# Basic Port Scanner

A simple Python port scanner that can check for open ports on a target IP address.

## DISCLAIMER
**This tool is for educational purposes only.** Only scan networks and devices you own or have EXPLICIT permission to as unauthorized scanning may violate laws and terms of service.

## Features

- Scans common ports
- Command line interface
- Fast scanning

## Requirements

- Python 3 or newer

## How to use tool

1. Clone or download this repository
2. Open a terminal in the project directory
3. Run "python port_scanner.py (target_ip)"

Example:
- python port_scanner.py 192.168.1.1


## What it does

The scanner attempts to connect to each of the ports on the list. If the connection is successful, the port is open. Otherwise, it's closed.

## Learning Outcomes

This project demonstrates:
- Basic socket programming in Python
- Network scanning concepts
- Error handling

## Future Improvements

- Add custom port ranges
- Service detection (what service is running on open ports)
- Multi-threading for faster scans
- Save results to a file

## Contributing

This is my first project so feel free to fork and improve this project, pull requests are welcome!

I may also forget about this project so please understand if this goes unupdated.
## License

MIT License - see LICENSE file for details.
