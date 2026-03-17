import subprocess

def sudo_users():

    r = subprocess.run(
        ["getent", "group", "sudo"],
        capture_output=True,
        text=True
    )

    if ":" in r.stdout:
        return r.stdout.strip().split(":")[-1].split(",")

    return []
