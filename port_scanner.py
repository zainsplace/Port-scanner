#!/usr/bin/env python3
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

PORT_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S", 3389: "RDP"
}

def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            return port, sock.connect_ex((target_ip, port)) == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return port, False

def main():
    while True:
        target_ip = input("Input the IP: ").strip()
        if valid_ip(target_ip):
            break
        print("Invalid IP address. Please enter a valid IPv4 address (e.g. 192.168.1.1)\n")

    ports = list(PORT_SERVICES.keys())
    print(f"\nScanning {target_ip} for open ports...")
    print("This may take a few seconds.\n")
    results = {}
    with ThreadPoolExecutor(max_workers=len(ports)) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in ports}
        for future in as_completed(futures):
            port, is_open = future.result()
            results[port] = is_open
    open_ports = []
    for port in sorted(results):
        service = PORT_SERVICES.get(port, "Unknown")
        status = "OPEN" if results[port] else "CLOSED"
        print(f"Port {port} ({service}) is {status}")
        if results[port]:
            open_ports.append(port)
    print(f"\nScan complete. Found {len(open_ports)} open ports: {open_ports}")

if __name__ == "__main__":
    main()
