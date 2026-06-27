import urllib.request
import ssl

def check_headers(url):
    if not url.startswith("http"):
        url = "https://" + url
    
    print(f"\n=== Checking: {url} ===\n")
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        req = urllib.request.urlopen(url, context=ctx, timeout=10)
        headers = dict(req.headers)
    except Exception as e:
        print(f"Error: {e}")
        return

    security_headers = {
        "strict-transport-security": "HSTS",
        "content-security-policy": "CSP",
        "x-frame-options": "Clickjacking Protection",
        "x-content-type-options": "MIME Sniffing Protection",
        "referrer-policy": "Referrer Policy",
        "permissions-policy": "Permissions Policy",
        "x-xss-protection": "XSS Protection"
    }

    print("[+] Security Headers:")
    for key, name in security_headers.items():
        if key in headers:
            print(f"  FOUND    {name}: {headers[key][:50]}")
        else:
            print(f"  MISSING  {name}")

    print("\n[+] Server Info:")
    for info in ["server", "x-powered-by", "x-aspnet-version"]:
        if info in headers:
            print(f"  {info}: {headers[info]}")

url = input("Website URL enter karo: ")
check_headers(url)
