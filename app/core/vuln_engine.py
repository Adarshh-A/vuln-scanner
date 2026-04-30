def analyze_services(services, config):
    findings = []

    for s in services:
        service = s.get("service")
        version = s.get("version", "")
        port = s.get("port")

        # 🔴 SSH Weak Version
        if service == "ssh":
            if "7." in version:
                findings.append({
                    "severity": "HIGH",
                    "title": "Outdated SSH Version",
                    "description": f"{version} is outdated",
                    "recommendation": "Upgrade to OpenSSH 9.x or later",
                    "port": port
                })
            else:
                findings.append({
                    "severity": "LOW",
                    "title": "SSH Service Detected",
                    "description": "Ensure strong authentication is enabled",
                    "recommendation": "Disable password login, use key-based auth",
                    "port": port
                })

        # 🟠 HTTP
        if service == "http":
            findings.append({
                "severity": "MEDIUM",
                "title": "Unencrypted HTTP Service",
                "description": f"HTTP running on port {port}",
                "recommendation": "Redirect HTTP to HTTPS",
                "port": port
            })

        # 🔴 FTP
        if service == "ftp":
            findings.append({
                "severity": "HIGH",
                "title": "Insecure FTP Service",
                "description": "FTP transmits data in plaintext",
                "recommendation": "Disable FTP or use SFTP",
                "port": port
            })

        # 🟡 HTTPS (best practice check)
        if service == "https":
            findings.append({
                "severity": "LOW",
                "title": "HTTPS Service Detected",
                "description": "Check SSL/TLS configuration",
                "recommendation": "Use strong TLS (1.2+), disable weak ciphers",
                "port": port
            })

    return findings
