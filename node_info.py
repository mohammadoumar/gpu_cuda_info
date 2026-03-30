import platform
import socket
import os
import subprocess
import psutil


def section(title):
    print(f"\n=== {title} ===")


def print_basic():
    section("Node Identity")
    print(f"  Hostname:       {socket.gethostname()}")
    print(f"  FQDN:           {socket.getfqdn()}")
    print(f"  OS:             {platform.system()} {platform.release()}")
    print(f"  OS Version:     {platform.version()}")
    print(f"  Architecture:   {platform.machine()}")
    print(f"  Python:         {platform.python_version()}")


def print_cpu():
    section("CPU")
    print(f"  Model:          {platform.processor() or 'N/A'}")
    print(f"  Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"  Logical cores:  {psutil.cpu_count(logical=True)}")
    freq = psutil.cpu_freq()
    if freq:
        print(f"  Max Frequency:  {freq.max:.0f} MHz")
        print(f"  Current Freq:   {freq.current:.0f} MHz")
    print(f"  CPU Usage:      {psutil.cpu_percent(interval=1)}%")
    load = os.getloadavg()
    print(f"  Load Avg (1/5/15 min): {load[0]:.2f} / {load[1]:.2f} / {load[2]:.2f}")


def print_memory():
    section("Memory")
    vm = psutil.virtual_memory()
    sw = psutil.swap_memory()
    print(f"  Total RAM:      {vm.total / 1024**3:.2f} GB")
    print(f"  Available RAM:  {vm.available / 1024**3:.2f} GB")
    print(f"  Used RAM:       {vm.used / 1024**3:.2f} GB ({vm.percent}%)")
    print(f"  Swap Total:     {sw.total / 1024**3:.2f} GB")
    print(f"  Swap Used:      {sw.used / 1024**3:.2f} GB ({sw.percent}%)")


def print_disk():
    section("Disk")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"  {part.mountpoint} ({part.fstype}): "
                  f"{usage.total / 1024**3:.1f} GB total, "
                  f"{usage.used / 1024**3:.1f} GB used ({usage.percent}%)")
        except PermissionError:
            pass


def print_network():
    section("Network Interfaces")
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    for iface, addr_list in addrs.items():
        up = stats[iface].isup if iface in stats else False
        for addr in addr_list:
            if addr.family == socket.AF_INET:
                print(f"  {iface} ({'UP' if up else 'DOWN'}): {addr.address}")


def print_slurm():
    section("SLURM Environment")
    slurm_vars = [
        "SLURM_JOB_ID", "SLURM_JOB_NAME", "SLURM_NODELIST",
        "SLURM_NTASKS", "SLURM_CPUS_ON_NODE", "SLURM_MEM_PER_NODE",
        "SLURM_JOB_PARTITION", "SLURM_JOB_NODELIST"
    ]
    found = False
    for var in slurm_vars:
        val = os.environ.get(var)
        if val:
            print(f"  {var}: {val}")
            found = True
    if not found:
        print("  Not running inside a SLURM job.")


if __name__ == "__main__":
    print_basic()
    print_cpu()
    print_memory()
    print_disk()
    print_network()
    print_slurm()
