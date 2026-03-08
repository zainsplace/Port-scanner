#!/usr/bin/env python3
"""
Basic Port Scanner
A simple tool to scan for open ports on a target IP address.
Use responsibly and only on networks you own or have permission to scan.

Author: Zain
"""

import socket
import sys
import time

def scan_port(target_ip, port):
    """
    Scan a single port on the target IP.
    Returns True if open, False if closed.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second

        # Attempt to connect
        result = sock.connect_ex((target_ip, port))

        # Close the socket
        sock.close()

        # If result is 0, port is open
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

    # Common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3389]

    print(f"Scanning {target_ip} for open ports...")
    print("This may take a few seconds.\n")

    open_ports = []

    for port in common_ports:
        if scan_port(target_ip, port):
            open_ports.append(port)
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

    print(f"\nScan complete. Found {len(open_ports)} open ports: {open_ports}")

if __name__ == "__main__":
    main()