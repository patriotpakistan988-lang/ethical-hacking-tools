import subprocess
import socket
import re

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "192.168.1.1"

def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except:
        return False

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

local_ip = get_local_ip()
parts = local_ip.split(".")
network = f"{parts[0]}.{parts[1]}.{parts[2]}"

print(f"=== Network Scanner ===")
print(f"Aapka IP: {local_ip}")
print(f"Network: {network}.0/24")
print(f"Scanning... (thoda time lagega)\n")

live_hosts = []
for i in range(1, 255):
    ip = f"{network}.{i}"
    if ping_host(ip):
        hostname = get_hostname(ip)
        live_hosts.append(ip)
        print(f"[+] {ip} - {hostname}")

print(f"\nTotal devices mile: {len(live_hosts)}")
