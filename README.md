# 🛡️ Automated Financial Reconciliation Engine

A modular Python-based auditing system designed to identify data drift and financial discrepancies between internal ledgers and third-party payment gateways.

---

## 🎯 The Business Case
In production environments, data is never perfect. Network timeouts, partial refunds, and duplicate API calls create "data drift" between what a company thinks it earned and what the bank actually received. 

This engine automates the "Truth-Finding" process, moving from manual spreadsheet checks to a **systematic, code-driven audit.**

---

## 🚀 Key Features
* **Chaos Engineering:** Uses the `Faker` library to generate synthetic "Source of Truth" data and injects purposeful errors (missing rows, amount drift, duplicates) for testing.
* **Modular Architecture:** Clean separation of concerns between Data Generation (`generator.py`), Logic (`auditor.py`), and Execution (`main.py`).
* **Automated Auditing:** Utilizes Pandas join strategies to categorize errors: *Missing*, *Mismatch*, and *Duplicate*.
* **Stakeholder Reporting:** Generates a professional, color-coded Excel report with conditional formatting.

---

## 📁 Project Structure
```text
Automated-Financial-Auditor/
├── data/               # Raw CSV exports (Internal vs. Gateway)
├── reports/            # Final Styled Excel Audit Reports
├── src/
│   ├── generator.py    # Synthetic data & chaos injection engine
│   └── auditor.py      # Pandas-based reconciliation logic
├── notebook/           # Visual walkthrough and prototyping
├── main.py             # Pipeline orchestrator (Entry Point)
├── requirements.txt    # Project dependencies
└── README.md
```

## 📸 Proof of Concept: The Audit Flow

### 1. The "Red Flag" Analysis (Mismatches & Missing)
The engine programmatically identifies and highlights issues. Below, the red rows indicate **Amount Mismatches** (discrepancies between internal records and the gateway), while yellow indicates records **Missing in Gateway**.

<img width="1143" height="612" alt="aa" src="https://github.com/user-attachments/assets/dca2ed6e-3a0c-4590-bb90-6dc55afb9377" />


### 2. Identifying Concurrency Issues (Duplicates)
The auditor also catches **Duplicates**, where a single Transaction ID appears twice in the gateway statement, which could signify a double-charge error.

<img width="1100" height="602" alt="aa2" src="https://github.com/user-attachments/assets/ffb5afc3-be71-4b55-b6fd-ea8887238257" />


### 3. Final Stakeholder Delivery
The logic is exported into a portable Excel format, ensuring that the findings are accessible to non-technical stakeholders (Finance/Accounting teams).
