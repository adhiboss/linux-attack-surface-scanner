import subprocess

def running_services():

    r = subprocess.run(
        ["systemctl", "list-units", "--type=service", "--state=running"],
        capture_output=True,
        text=True
    )

    services = []

    for line in r.stdout.splitlines():

        if ".service" in line:
            services.append(line.split()[0])

    return services
