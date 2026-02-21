import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class ReconAuditor:
    def __init__(self):
        self.comparison_df = None

    def reconcile(self, internal_df, gateway_df):
        logging.info("Analyzing data for discrepancies...")

        gateway_df = gateway_df.copy()
        gateway_df['is_duplicate'] = gateway_df.duplicated(subset=['TX_ID'], keep=False)

        merged = pd.merge(
            internal_df,
            gateway_df[['TX_ID', 'Amount', 'is_duplicate']],
            on="TX_ID",
            how="left",
            suffixes=('_int', '_gat')
        )

        def flag_issue(row):
            if pd.isna(row['Amount_gat']):
                return "MISSING_IN_GATEWAY"
            if row['is_duplicate']:
                return "DUPLICATE_IN_GATEWAY"
            if row['Amount_int'] != row['Amount_gat']:
                return "AMOUNT_MISMATCH"
            return "MATCH"

        merged['Audit_Status'] = merged.apply(flag_issue, axis=1)
        self.comparison_df = merged

        stats = merged['Audit_Status'].value_counts()
        logging.info(f"Audit Complete. Found: {stats.to_dict()}")
        return merged

    def export_report(self, output_path="reports/Reconciliation_Report.xlsx"):
        if self.comparison_df is None:
            raise ValueError("No audit data found. Run reconcile() first.")

        if not os.path.exists("reports"):
            os.makedirs("reports")

        def highlight_errors(row):
            styles = [''] * len(row)
            status = row['Audit_Status']

            if status == "AMOUNT_MISMATCH":
                color = 'background-color: #ffcccc'  # Red-ish
            elif status == "MISSING_IN_GATEWAY":
                color = 'background-color: #ffffcc'  # Yellow-ish
            elif status == "DUPLICATE_IN_GATEWAY":
                color = 'background-color: #cce5ff'  # Blue-ish
            else:
                return styles  # No style for matches

            return [color for _ in range(len(row))]

        styled_df = self.comparison_df.style.apply(highlight_errors, axis=1)
        styled_df.to_excel(output_path, engine='openpyxl', index=False)
        logging.info(f"High-fidelity report exported to {output_path}")