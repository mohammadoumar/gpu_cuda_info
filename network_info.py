import socket
import psutil


def section(title):
    print(f"\n=== {title} ===")


def print_hostname():
    section("Hostname")
    print(f"  Hostname:       {socket.gethostname()}")
    print(f"  FQDN:           {socket.getfqdn()}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"  Primary IP:     {ip}")
    except socket.gaierror:
        print(f"  Primary IP:     N/A")


def print_interfaces():
    section("Network Interfaces")
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for iface, addr_list in sorted(addrs.items()):
        st = stats.get(iface)
        status = "UP" if st and st.isup else "DOWN"
        speed = f"{st.speed} Mbps" if st and st.speed > 0 else "N/A"
        mtu = st.mtu if st else "N/A"
        print(f"\n  [{iface}]  status={status}  speed={speed}  mtu={mtu}")

        for addr in addr_list:
            if addr.family == socket.AF_INET:
                mask = f"  netmask={addr.netmask}" if addr.netmask else ""
                bcast = f"  broadcast={addr.broadcast}" if addr.broadcast else ""
                print(f"    IPv4:  {addr.address}{mask}{bcast}")
            elif addr.family == socket.AF_INET6:
                print(f"    IPv6:  {addr.address}")
            else:
                # MAC address (AF_PACKET on Linux)
                print(f"    MAC:   {addr.address}")


def print_io_counters():
    section("Network I/O Counters")
    counters = psutil.net_io_counters(pernic=True)
    header = f"  {'Interface':<16} {'Bytes Sent':>14} {'Bytes Recv':>14} {'Pkts Sent':>12} {'Pkts Recv':>12} {'Errs In':>8} {'Errs Out':>8}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for iface, c in sorted(counters.items()):
        print(
            f"  {iface:<16} {c.bytes_sent:>14,} {c.bytes_recv:>14,} "
            f"{c.packets_sent:>12,} {c.packets_recv:>12,} "
            f"{c.errin:>8} {c.errout:>8}"
        )


def print_connections():
    section("Active TCP Connections")
    try:
        conns = psutil.net_connections(kind="tcp")
    except psutil.AccessDenied:
        print("  Access denied — run as root for full connection list.")
        return

    established = [c for c in conns if c.status == "ESTABLISHED"]
    listening = [c for c in conns if c.status == "LISTEN"]

    print(f"  Established:    {len(established)}")
    print(f"  Listening:      {len(listening)}")

    if listening:
        print()
        print(f"  {'Local Address':<30} {'PID':>8}")
        print("  " + "-" * 40)
        for c in sorted(listening, key=lambda x: x.laddr.port if x.laddr else 0):
            addr = f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else "N/A"
            pid = str(c.pid) if c.pid else "N/A"
            print(f"  {addr:<30} {pid:>8}")


if __name__ == "__main__":
    print_hostname()
    print_interfaces()
    print_io_counters()
    print_connections()
