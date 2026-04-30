import yaml
from app.scanner.port_scanner import scan_target
from app.core.vuln_engine import analyze_services
from app.core.risk import calculate_risk
from app.utils.report import generate_report


def run(target):
    config = yaml.safe_load(open("config.yaml"))

    print("[+] Scanning target...")
    services = scan_target(target, config["scan"]["ports"])

    print("[+] Analyzing vulnerabilities...")
    findings = analyze_services(services, config)

    risk = calculate_risk(findings)

    report_file = generate_report(target, services, findings, risk)

    print(f"[+] Report saved: {report_file}")
