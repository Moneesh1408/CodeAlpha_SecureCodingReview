"""
                        TASK-3 : SECURE CODING REVIEW USING PYTHON
"""

import subprocess
import json
import sys

def run_security_scan(target_file):
    print(f"=== Starting Static Analysis on: {target_file} ===\n")
    
    # Executes the bandit command-line utility via Python subprocess
    result = subprocess.run(
        [sys.executable, "-m", "bandit", "-f", "json", target_file],
        capture_output=True,
        text=True
    )
    
    try:
        scan_data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("❌ Error: Bandit tool failed to output clean data.")
        return

    issues = scan_data.get("results", [])
    if not issues:
        print("🎉 Clean Scan! No safety bugs detected.")
        return

    print(f"⚠️ Flagged {len(issues)} code flaws:\n")
    for idx, issue in enumerate(issues, start=1):
        print(f"[{idx}] {issue['issue_text']}")
        print(f"    Line: {issue['line_number']} | Severity: {issue['issue_severity']}")
        print(f"    Code Segment: {issue['code'].strip()}\n")

if __name__ == "__main__":
    run_security_scan("vulnerable_code.py")
    run_security_scan("secure_code.py")