# CodeAlpha_Secure_Coding_Review

An automated Static Application Security Testing (SAST) tool framework developed in Python using the `bandit` security engine. This project establishes a programmatic automation pipeline that scans python code scripts, detects structural security vulnerabilities, and generates actionable, clean developer reports to demonstrate a complete secure coding remediation lifecycle.

Developed as part of the **CodeAlpha Cybersecurity Internship Program** to demonstrate a hands-on understanding of code-level security flaws, static code analysis methods, and enterprise-grade software hardening practices.

---

# Author
**Moneesh Kumar T**,  
**CyberSecurity Intern** At **CodeAlpha**.

---

## 🚀 Features

* **Multi-File Automated Auditing:** Programmatically loops and executes automated structural scans sequentially over multiple target modules.
* **Abstract Syntax Tree (AST) Parsing:** Leverages static analysis to evaluate the programmatic logic framework of the code, going beyond simple regular expression patterns.
* **CWE Vulnerability Detection:** Successfully flags critical security holes including **Insecure Cryptographic Algorithms (CWE-327)** and **SQL Injection Vectors (CWE-89)**.
* **Clean Diagnostic Reporting:** Extracts raw backend JSON audit trails and transforms them into organized developer console outputs displaying line numbers and risk severity levels.

---

## 🛠️ Requirements & Installation

### 1. Python Environment & Core Engines
This project requires Python 3.x. The automation runner framework interfaces directly with the Flask web environment, the database connector engine, and the static application analyzer.

Install all system dependencies simultaneously using `pip`:

```bash
pip install bandit flask bcrypt
