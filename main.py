from src.generator import DataGenerator
from src.auditor import ReconAuditor
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def run_pipeline():
    logging.info("--- Starting Financial Reconciliation Pipeline ---")

    gen = DataGenerator(seed=42)
    internal_data = gen.create_base_data(n=1000)
    gateway_data = gen.inject_chaos(missing_count=5, mismatch_count=3, duplicate_count=2)

    gen.save_to_csv(folder="data")

    auditor = ReconAuditor()
    auditor.reconcile(internal_data, gateway_data)

    auditor.export_report(output_path="reports/Final_Audit_Report.xlsx")

    logging.info("--- Pipeline Execution Successful ---")
    print("\n👉 Check the 'reports/' folder for the color-coded Excel file!")


if __name__ == "__main__":
    run_pipeline()