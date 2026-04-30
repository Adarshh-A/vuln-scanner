from datetime import datetime
import re
import os


def clean_target(target):
    # remove protocol
    target = target.replace("http://", "").replace("https://", "")
    target = target.strip("/")

    # replace invalid characters
    return re.sub(r'[^a-zA-Z0-9.-]', '_', target)


def generate_report(target, services, findings, risk):
    safe_target = clean_target(target)

    # ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    report = f"""
==================================================
        VULNERABILITY ASSESSMENT REPORT
==================================================

Target: {target}
Scan Date: {datetime.now()}
Overall Risk Level: {risk}

-------------------------------
OPEN PORTS & SERVICES
-------------------------------
"""

    for s in services:
        report += f"""
Port: {s['port']}
Service: {s['service']}
Version: {s['version']}
--------------------------------
"""

    report += "\n-------------------------------\nVULNERABILITIES\n-------------------------------\n"

    if not findings:
        report += """
No critical vulnerabilities detected.

Note:
- Ensure services are regularly updated
- Apply security patches
- Perform periodic security audits
"""
    else:
        for f in findings:
            report += f"""
[{f['severity']}] {f['title']}
Port: {f['port']}
Description: {f['description']}
Recommendation: {f['recommendation']}
--------------------------------
"""

    report += "\n============== END OF REPORT ==============\n"

    filename = f"reports/{safe_target}_report.txt"

    with open(filename, "w") as file:
        file.write(report)

    return filename
