import subprocess

def scan_ports():
    result = subprocess.run(["ss","-tuln"],capture_output=True,text=True)
    lines = result.stdout.splitlines()[1:]
    ports=set()

    for l in lines:
        parts=l.split()
        if len(parts)>=5:
            port=parts[4].split(":")[-1]
            ports.add(port)

    return sorted(list(ports))
