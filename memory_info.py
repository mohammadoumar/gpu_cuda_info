import os
import sys
import psutil


def section(title):
    print(f"\n=== {title} ===")


def _gb(value):
    return f"{value / 1024**3:.2f} GB"


def _bar(percent, width=30):
    filled = int(width * percent / 100)
    return f"[{'#' * filled}{'.' * (width - filled)}] {percent:.1f}%"


def print_virtual_memory():
    section("Virtual Memory (RAM)")
    vm = psutil.virtual_memory()
    print(f"  Total:          {_gb(vm.total)}")
    print(f"  Available:      {_gb(vm.available)}")
    print(f"  Used:           {_gb(vm.used)}  {_bar(vm.percent)}")
    print(f"  Free:           {_gb(vm.free)}")
    print(f"  Cached:         {_gb(getattr(vm, 'cached', 0))}")
    print(f"  Buffers:        {_gb(getattr(vm, 'buffers', 0))}")
    print(f"  Shared:         {_gb(getattr(vm, 'shared', 0))}")


def print_swap():
    section("Swap Memory")
    sw = psutil.swap_memory()
    if sw.total == 0:
        print("  No swap configured.")
        return
    print(f"  Total:          {_gb(sw.total)}")
    print(f"  Used:           {_gb(sw.used)}  {_bar(sw.percent)}")
    print(f"  Free:           {_gb(sw.free)}")
    print(f"  Swapped In:     {_gb(sw.sin)}")
    print(f"  Swapped Out:    {_gb(sw.sout)}")


def print_meminfo():
    """Parse /proc/meminfo for detailed kernel memory breakdown (Linux only)."""
    if not sys.platform.startswith("linux"):
        return
    section("Kernel Memory Breakdown (/proc/meminfo)")
    keys_of_interest = [
        "MemTotal", "MemFree", "MemAvailable", "Buffers", "Cached",
        "SwapCached", "Active", "Inactive", "Active(anon)", "Inactive(anon)",
        "Active(file)", "Inactive(file)", "Unevictable", "Mlocked",
        "SwapTotal", "SwapFree", "Dirty", "Writeback", "AnonPages",
        "Mapped", "Shmem", "KReclaimable", "Slab", "SReclaimable",
        "SUnreclaim", "HugePages_Total", "HugePages_Free", "Hugepagesize",
    ]
    try:
        meminfo = {}
        with open("/proc/meminfo", encoding="utf-8") as f:
            for line in f:
                parts = line.split()
                key = parts[0].rstrip(":")
                val = int(parts[1]) if len(parts) >= 2 and parts[1].isdigit() else None
                meminfo[key] = val

        col_w = 24
        for key in keys_of_interest:
            if key in meminfo and meminfo[key] is not None:
                val_kb = meminfo[key]
                val_gb = val_kb / 1024**2
                print(f"  {key:<{col_w}} {val_gb:>8.2f} GB  ({val_kb:,} kB)")
    except FileNotFoundError:
        pass


def print_top_processes():
    section("Top 10 Processes by Memory Usage")
    procs = []
    for p in psutil.process_iter(["pid", "name", "memory_info", "memory_percent"]):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procs.sort(key=lambda x: x["memory_percent"] or 0, reverse=True)
    print(f"  {'PID':>8}  {'Name':<25} {'RSS':>10} {'VMS':>10} {'Mem%':>7}")
    print("  " + "-" * 65)
    for p in procs[:10]:
        rss = _gb(p["memory_info"].rss) if p["memory_info"] else "N/A"
        vms = _gb(p["memory_info"].vms) if p["memory_info"] else "N/A"
        pct = f"{p['memory_percent']:.2f}%" if p["memory_percent"] else "N/A"
        print(f"  {p['pid']:>8}  {(p['name'] or 'N/A'):<25} {rss:>10} {vms:>10} {pct:>7}")


if __name__ == "__main__":
    print_virtual_memory()
    print_swap()
    print_meminfo()
    print_top_processes()
