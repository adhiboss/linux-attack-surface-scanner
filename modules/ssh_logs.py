import subprocess

def failed_logins():
    r=subprocess.run(
        ["grep","Failed password","/var/log/auth.log"],
        capture_output=True,text=True
    )
    return len(r.stdout.splitlines())
