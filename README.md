# Vulnerability Scanner

Vulnerability scanner sederhana ini dapat digunakan untuk mendeteksi potensi kerentanan **SQL Injection** dan **Cross-Site Scripting (XSS)** di website. Scanner ini menggunakan Python dan library `requests` serta `beautifulsoup4`.

## Fitur
- **SQL Injection**: Menguji form pada halaman website untuk kerentanan SQL Injection.
- **Cross-Site Scripting (XSS)**: Menguji form pada halaman website untuk kerentanan XSS.

## Cara Menggunakan

### 1. Clone Repository
Pertama, clone repository ini ke mesin lokal Anda:
```bash
git clone https://github.com/MChaidirSyam/vuln-scanner.git
cd vuln-scanner
pip install requests beautifulsoup4
python vuln_scanner.py
Enter the URL to scan: http://example.com

