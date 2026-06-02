import platform
import os
import sys
import datetime
import subprocess

import psutil


def section(title):
    print(f"\n=== {title} ===")


def print_os_identity():
    section("OS Identity")
    print(f"  System:         {platform.system()}")
    print(f"  Release:        {platform.release()}")
    print(f"  Version:        {platform.version()}")
    print(f"  Platform:       {platform.platform()}")
    print(f"  Architecture:   {platform.machine()} / {platform.architecture()[0]}")

    # Linux distro info via /etc/os-release
    if sys.platform.startswith("linux"):
        os_release = {}
        try:
            with open("/etc/os-release", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if "=" in line and not line.startswith("#"):
                        k, v = line.split("=", 1)
                        os_release[k] = v.strip('"')
        except FileNotFoundError:
            pass
        if os_release:
            print(f"  Distro:         {os_release.get('PRETTY_NAME', 'N/A')}")
            print(f"  Distro ID:      {os_release.get('ID', 'N/A')}")
            print(f"  Distro Version: {os_release.get('VERSION_ID', 'N/A')}")


def print_kernel():
    section("Kernel")
    print(f"  Kernel release: {platform.release()}")
    print(f"  Kernel version: {platform.version()}")
    try:
        result = subprocess.run(["uname", "-r"], capture_output=True, text=True)
        print(f"  uname -r:       {result.stdout.strip()}")
    except FileNotFoundError:
        pass


def print_uptime():
    section("Uptime & Boot")
    boot_ts = psutil.boot_time()
    boot_dt = datetime.datetime.fromtimestamp(boot_ts)
    now = datetime.datetime.now()
    uptime = now - boot_dt
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes = remainder // 60
    print(f"  Boot time:      {boot_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Uptime:         {days}d {hours}h {minutes}m")


def print_python():
    section("Python Runtime")
    print(f"  Version:        {platform.python_version()}")
    print(f"  Implementation: {platform.python_implementation()}")
    print(f"  Executable:     {sys.executable}")
    print(f"  Prefix:         {sys.prefix}")


def print_locale():
    section("Locale & Timezone")
    tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    print(f"  Timezone:       {tz}")
    print(f"  LANG:           {os.environ.get('LANG', 'N/A')}")
    print(f"  LC_ALL:         {os.environ.get('LC_ALL', 'N/A')}")


def print_env():
    section("Key Environment Variables")
    keys = ["HOME", "USER", "SHELL", "PATH", "VIRTUAL_ENV", "CONDA_DEFAULT_ENV",
            "TMPDIR", "XDG_RUNTIME_DIR"]
    for k in keys:
        val = os.environ.get(k)
        if val:
            display = val if len(val) <= 80 else val[:77] + "..."
            print(f"  {k:<20} {display}")


if __name__ == "__main__":
    print_os_identity()
    print_kernel()
    print_uptime()
    print_python()
    print_locale()
    print_env()
