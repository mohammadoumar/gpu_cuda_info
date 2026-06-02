import os
import sys
import subprocess
import psutil


def section(title):
    print(f"\n=== {title} ===")


def _gb(value):
    return f"{value / 1024**3:.2f} GB"


def _bar(percent, width=30):
    filled = int(width * percent / 100)
    return f"[{'#' * filled}{'.' * (width - filled)}] {percent:.1f}%"


def print_partitions():
    section("Disk Partitions & Usage")
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue
        print(f"\n  {part.mountpoint}")
        print(f"    Device:     {part.device}")
        print(f"    Filesystem: {part.fstype}")
        print(f"    Options:    {part.opts}")
        print(f"    Total:      {_gb(usage.total)}")
        print(f"    Used:       {_gb(usage.used)}  {_bar(usage.percent)}")
        print(f"    Free:       {_gb(usage.free)}")


def print_io_counters():
    section("Disk I/O Counters")
    counters = psutil.disk_io_counters(perdisk=True)
    if not counters:
        print("  No I/O counters available.")
        return
    header = f"  {'Device':<16} {'Reads':>10} {'Writes':>10} {'Read Bytes':>14} {'Write Bytes':>14} {'Read Time':>12} {'Write Time':>12}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for dev, c in sorted(counters.items()):
        print(
            f"  {dev:<16} {c.read_count:>10,} {c.write_count:>10,} "
            f"{_gb(c.read_bytes):>14} {_gb(c.write_bytes):>14} "
            f"{c.read_time:>10} ms {c.write_time:>10} ms"
        )


def print_block_devices():
    """List block devices via lsblk (Linux only)."""
    if not sys.platform.startswith("linux"):
        return
    section("Block Devices (lsblk)")
    try:
        result = subprocess.run(
            ["lsblk", "-o", "NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT,MODEL,ROTA"],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines():
            print(f"  {line}")
    except FileNotFoundError:
        print("  lsblk not available.")


def print_inodes():
    """Show inode usage per mount (Linux only via /proc/mounts + statvfs)."""
    if not sys.platform.startswith("linux"):
        return
    section("Inode Usage")
    print(f"  {'Mountpoint':<30} {'Total Inodes':>15} {'Used':>12} {'Free':>12} {'Use%':>7}")
    print("  " + "-" * 78)
    seen = set()
    for part in psutil.disk_partitions(all=False):
        if part.mountpoint in seen:
            continue
        seen.add(part.mountpoint)
        try:
            st = os.statvfs(part.mountpoint)
            total = st.f_files
            free = st.f_ffree
            used = total - free
            pct = (used / total * 100) if total > 0 else 0.0
            print(f"  {part.mountpoint:<30} {total:>15,} {used:>12,} {free:>12,} {pct:>6.1f}%")
        except (PermissionError, OSError):
            pass


if __name__ == "__main__":
    print_partitions()
    print_io_counters()
    print_block_devices()
    print_inodes()
