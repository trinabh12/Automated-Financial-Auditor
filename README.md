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
