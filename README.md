# port-scanner

PyPortScanner is a lightweight and efficient Python-based tool designed for quickly identifying open ports on a target host. This tool is ideal for network administrators, penetration testers, and cybersecurity professionals who need to scan networks to discover open ports and assess network security.


Current Features:
Port Scanning: PyPortScanner currently offers robust port scanning capabilities, allowing users to specify a range of ports to scan on a given host. The tool efficiently checks for open ports and reports them back to the user.

Upcoming Features:
Banner Grabbing: We are actively working on implementing a banner grabbing feature, which will allow PyPortScanner to retrieve service banners from open ports. This can provide valuable information about the services running on those ports.
Service Detection: Future updates will include service detection capabilities, enabling the tool to identify and report the specific services running on open ports.
OS Fingerprinting: We plan to add OS fingerprinting functionality, allowing the tool to infer the operating system of the target host based on network responses.
Vulnerability Scanning: Another planned feature is the integration of a basic vulnerability scanner that will check for common vulnerabilities associated with identified services.

Future Goals:
Our goal is to evolve PyPortScanner into a comprehensive network scanning toolkit, providing users with an all-in-one solution for network reconnaissance and vulnerability assessment. Stay tuned for more updates and features as we continue to develop and enhance the tool.


## Table of Contents

- [Features](#features-✨)
- [Installation](#installation)
- [Usage](#usage)



## Features ✨

- 🚀 Fast and efficient
- 🔒 Secure
- 💻 Cross-platform

## Installation 
```bash
Clone the repository:
git clone https://github.com/harshityadav7/port-scanner.git
cd repository
Then, change the permissions to make it executable:
chmod +x port_scanner.py

## USAGE
./port_scanner.py <host> --start_port --end_port
Specify the ports after writing --Start_port and --end_port parameters
example usage ./port_scanner.py 192.168.1.1 --start_port 1 --end_port 1000










