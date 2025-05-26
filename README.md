# 🕵️‍♂️ data_exfil: A Simulated Data Exfiltration Tool (Educational Use Only)

# WIP (WORK IN PROGRESS)

**data_exfil** is a Python-based educational tool that simulates data exfiltration over FTP. It is designed for use in ethical hacking labs, red team exercises, and personal cybersecurity research. This project was developed by a BCIT student as part of a self-directed summer learning project.

> ⚠️ **Disclaimer**: This tool is intended for use in authorized environments only. Do **not** use it on any network, system, or data you do not own or have explicit permission to test. Unauthorized use is illegal and unethical.

---

## 🔍 Features

- Monitors specified directories for file types of interest  
- Automatically exfiltrates matching files to a simulated Command & Control (C2) FTP server  
- Supports `.docx`, `.xlsx`, `.pdf`, `.png`, `.txt`, and other file types  
- Can be adapted for blue team training (e.g., detecting anomalous outbound traffic)

---

## 📦 Requirements

- Python 3.8+  
- pip install -r requirements.txt

---

## ⚙️ Setup

1. Clone the repo:

```bash
git clone https://github.com/your-username/ftpexfil.git
cd data_exfil
```

2. Configure your `.env` file:

```
CONNECT_IP=127.0.0.1
FTP_USER=youruser
FTP_PASS=yourpass
```

## 🧪 Use Cases (Legal & Ethical Only)

- Penetration testing labs  
- Blue team detection tuning  
- Red team simulation  
- Learning about threat actor behaviors in a safe lab

---

## 🛡️ Ethical Notice

This project exists solely to help students and professionals understand, simulate, and defend against real-world threat techniques. Misusing this tool outside of approved environments is both illegal and unethical.

---

## 📜 License

MIT License — For educational and authorized use only.

---

## 👨‍🎓 Author

Jack Fleming  
BCIT Summer Student  
Cybersecurity Enthusiast
