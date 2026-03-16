# Linux Attack Surface Scanner

Linux Attack Surface Scanner is a lightweight terminal reconnaissance tool that analyzes a Linux machine and reveals its potential exposure points. The goal of this project is to understand how security engineers and infrastructure teams quickly inspect a system for risky configurations.

Instead of being a full security framework, this tool focuses on visibility — showing what parts of a system are potentially accessible or exposed.

## What It Scans

The scanner inspects several areas that commonly contribute to a system's attack surface:

- Open network ports
- Running system services
- Privileged users (sudo access)
- SSH authentication failures
- Firewall configuration
- Login activity
- Listening processes

These checks help identify services or configurations that could be exploited if improperly secured.

## Why This Project Exists

When learning Linux infrastructure and security, one of the most important skills is understanding **what parts of a system are exposed to the outside world**.

This project was built as an experiment to explore how engineers quickly gather that information directly from the terminal.

## Example Output
LINUX ATTACK SURFACE SCAN

Open Ports:
22/tcp
80/tcp

Running Services:
ssh
systemd
networkd

Firewall Status:
active

Recent Login Attempts:
user1
user2


## Technologies Used

- Bash
- Linux system utilities
- Core networking tools
- System log inspection

## Usage


chmod +x attack-surface-scan.sh
./attack-surface-scan.sh


## Learning Focus

This project explores concepts related to:

- Linux system inspection
- infrastructure visibility
- security exposure awareness
- terminal-based tooling
