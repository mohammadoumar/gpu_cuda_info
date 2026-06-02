import os
import sys
import datetime
import psutil


def section(title):
    print(f"\n=== {title} ===")


def _gb(value):
    return f"{value / 1024**3:.2f} GB"


def _elapsed(create_time):
    try:
        started = datetime.datetime.fromtimestamp(create_time)
        delta = datetime.datetime.now() - started
        h, rem = divmod(int(delta.total_seconds()), 3600)
        m, s = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"
    except Exception:
        return "N/A"


def print_summary():
    section("Process Summary")
    procs = list(psutil.process_iter(["status"]))
    status_counts = {}
    for p in procs:
        try:
            st = p.info["status"]
            status_counts[st] = status_counts.get(st, 0) + 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    print(f"  Total processes: {len(procs)}")
    for status, count in sorted(status_counts.items()):
        print(f"    {status:<20} {count}")


def print_top_cpu():
    section("Top 10 Processes by CPU Usage")
    # Two-interval call to get meaningful cpu_percent values
    for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            p.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    import time
    time.sleep(0.5)

    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "status",
                                   "num_threads", "create_time"]):
        try:
            p.info["cpu_percent"] = p.cpu_percent(interval=None)
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procs.sort(key=lambda x: x["cpu_percent"] or 0, reverse=True)
    print(f"  {'PID':>8}  {'Name':<25} {'CPU%':>7} {'Threads':>8} {'Status':<12} {'Elapsed':>10}")
    print("  " + "-" * 75)
    for p in procs[:10]:
        elapsed = _elapsed(p.get("create_time"))
        print(
            f"  {p['pid']:>8}  {(p['name'] or 'N/A'):<25} "
            f"{p['cpu_percent']:>6.1f}% {p.get('num_threads', 0):>8} "
            f"{(p.get('status') or 'N/A'):<12} {elapsed:>10}"
        )


def print_top_memory():
    section("Top 10 Processes by Memory Usage")
    procs = []
    for p in psutil.process_iter(["pid", "name", "memory_info",
                                   "memory_percent", "username"]):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procs.sort(key=lambda x: x["memory_percent"] or 0, reverse=True)
    print(f"  {'PID':>8}  {'Name':<25} {'User':<15} {'RSS':>10} {'VMS':>10} {'Mem%':>7}")
    print("  " + "-" * 80)
    for p in procs[:10]:
        rss = _gb(p["memory_info"].rss) if p["memory_info"] else "N/A"
        vms = _gb(p["memory_info"].vms) if p["memory_info"] else "N/A"
        pct = f"{p['memory_percent']:.2f}%" if p["memory_percent"] else "N/A"
        user = (p.get("username") or "N/A")[:14]
        print(f"  {p['pid']:>8}  {(p['name'] or 'N/A'):<25} {user:<15} {rss:>10} {vms:>10} {pct:>7}")


def print_top_threads():
    section("Top 10 Processes by Thread Count")
    procs = []
    for p in psutil.process_iter(["pid", "name", "num_threads", "username"]):
        try:
            procs.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    procs.sort(key=lambda x: x["num_threads"] or 0, reverse=True)
    print(f"  {'PID':>8}  {'Name':<25} {'User':<15} {'Threads':>8}")
    print("  " + "-" * 60)
    for p in procs[:10]:
        user = (p.get("username") or "N/A")[:14]
        print(f"  {p['pid']:>8}  {(p['name'] or 'N/A'):<25} {user:<15} {p['num_threads']:>8}")


def print_open_files():
    section("Top 10 Processes by Open File Descriptors")
    procs = []
    for p in psutil.process_iter(["pid", "name"]):
        try:
            fds = p.num_fds()
            procs.append({"pid": p.pid, "name": p.name(), "fds": fds})
        except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
            pass

    procs.sort(key=lambda x: x["fds"], reverse=True)
    print(f"  {'PID':>8}  {'Name':<25} {'Open FDs':>10}")
    print("  " + "-" * 47)
    for p in procs[:10]:
        print(f"  {p['pid']:>8}  {p['name']:<25} {p['fds']:>10}")


if __name__ == "__main__":
    print_summary()
    print_top_cpu()
    print_top_memory()
    print_top_threads()
    print_open_files()
