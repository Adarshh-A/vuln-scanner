#  Vulnerability Scanner 

A professional-grade Python-based vulnerability scanner designed to identify common security issues in web applications and network services.

---

##  Features

*  Port scanning using Nmap
*  Service detection (HTTP, FTP, SSH, HTTPS)
*  Vulnerability identification
*  Risk classification (LOW / MEDIUM / HIGH / CRITICAL)
*  Automated report generation

---

##  Tech Stack

* Python 3
* Nmap
* PyYAML
* Requests

---

##  Project Structure

```
app/
 ├── core/          # Vulnerability engine
 ├── scanner/       # Port scanning logic
 ├── utils/         # Report generation
 └── main.py        # Entry point

config.yaml         # Configuration
run.sh              # Run script
```

---

##  Usage

```bash
chmod +x run.sh
./run.sh <target>
```

Example:

```bash
./run.sh 192.168.56.101
```

---

## 📄 Sample Output

```
[HIGH] Insecure FTP Service
Port: 21
Recommendation: Use SFTP instead of FTP
```

---

##  Purpose

This project demonstrates:

* Vulnerability assessment skills
* Network scanning techniques
* Security analysis & reporting

---

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only.
