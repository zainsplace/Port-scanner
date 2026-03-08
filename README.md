# Basic Port Scanner

A simple Python-based port scanner that checks for open ports on a target IP address.

## Disclaimer

**This tool is for educational purposes only.** Only scan networks and devices you own or have explicit permission to scan. Unauthorized scanning may violate laws and terms of service. Use at your own risk.

## Features

- Scans common ports (21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3389)
- Command-line interface
- Fast scanning with timeout

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository
2. Open a terminal in the project directory
3. Run: `python port_scanner.py <target_ip>`

Example:
```
python port_scanner.py 192.168.1.1
```

## What it does

The scanner attempts to connect to each port in the list. If the connection succeeds, the port is considered open. Otherwise, it's closed.

## Learning Outcomes

This project demonstrates:
- Basic socket programming in Python
- Network scanning concepts
- Command-line argument handling
- Error handling

## Future Improvements

- Add custom port ranges
- Service detection (what service is running on open ports)
- Multi-threading for faster scans
- Save results to a file

## Contributing

Feel free to fork and improve this project. Pull requests are welcome!

## License

MIT License - see LICENSE file for details.