from modules.ports import scan_ports
from modules.services import running_services
from modules.users import sudo_users
from modules.firewall import firewall_status
from modules.ssh_logs import failed_logins


def risk_score(ports, sudo, fw, fail):
    score = 0
    if len(ports) > 3:
        score += 3
    if len(sudo) > 1:
        score += 2
    if "inactive" in fw.lower():
        score += 3
    if fail > 5:
        score += 2
    return score


def main():
    ports = scan_ports()
    services = running_services()
    sudo = sudo_users()
    fw = firewall_status()
    fails = failed_logins()

    score = risk_score(ports, sudo, fw, fails)

    print("\nLINUX ATTACK SURFACE REPORT")
    print("=" * 35)

    print("\nOpen Ports:")
    for p in ports:
        print(" -", p)

    print("\nRunning Services:")
    for s in services[:5]:
        print(" -", s)

    print("\nSudo Users:", sudo)
    print("Firewall:", fw)
    print("Failed SSH Logins:", fails)

    print("\nExposure Score:", score, "/10")


if __name__ == "__main__":
    main()
