#!/usr/bin/env python3
import os
import socket
import sys
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def scan_port(target_ip, port):

    try:
       
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 

        result = sock.connect_ex((target_ip, port))

        sock.close()

        return result == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target_ip>")
        print("Example: python port_scanner.py 192.168.1.1")
        sys.exit(1)

    target_ip = sys.argv[1]

    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3389]

    port_services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
        443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S", 3389: "RDP"
    }

    print(f"Scanning {target_ip} for open ports...")
    print("This may take a few seconds.\n")

    open_ports = []

    for port in common_ports:
        service = port_services.get(port, "Unknown")
        if scan_port(target_ip, port):
            open_ports.append(port)
            print(f"Port {port} ({service}) is OPEN")
        else:
            print(f"Port {port} ({service}) is CLOSED")

    print(f"\nScan complete. Found {len(open_ports)} open ports: {open_ports}")

if __name__ == "__main__":
    main()
