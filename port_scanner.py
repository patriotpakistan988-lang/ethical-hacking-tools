import socket
import sys
from datetime import datetime

def scan(target, start, end):
    print(f"Scanning {target}")
    for port in range(start, end+1):
        sock = socket.socket()
        sock.settimeout(1)
        if sock.connect_ex((target, port)) == 0:
            print(f"Port {port}: OPEN")
        sock.close()

scan(input("Target: "), 1, 1000)
