import subprocess

def firewall_status():
    try:
        r = subprocess.run(["ufw", "status"], capture_output=True, text=True)
        lines = r.stdout.splitlines()
        if lines:
            return lines[0]
        else:
            return "Firewall status unavailable"
    except:
        return "UFW not installed"
