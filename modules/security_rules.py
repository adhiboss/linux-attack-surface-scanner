SUSPICIOUS_PORTS = {

    "23": "Telnet (insecure remote access)",
    "4444": "Common reverse shell port",
    "1337": "Backdoor / hacking tool port",
    "6667": "IRC botnet activity"

}


def check_ports(open_ports):

    warnings = []

    for p in open_ports:

        if p in SUSPICIOUS_PORTS:
            warnings.append((p, SUSPICIOUS_PORTS[p]))

    return warnings
