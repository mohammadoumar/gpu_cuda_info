import os
import subprocess


def section(title):
    print(f"\n=== {title} ===")


def _run(cmd):
    """Run a shell command and return stdout, or None on failure."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return result.stdout.strip() if result.returncode == 0 else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def _slurm_available():
    return _run(["sinfo", "--version"]) is not None


def print_job_env():
    section("Current SLURM Job Environment")
    slurm_vars = [
        "SLURM_JOB_ID", "SLURM_JOB_NAME", "SLURM_JOB_PARTITION",
        "SLURM_JOB_NODELIST", "SLURM_NODELIST", "SLURM_NNODES",
        "SLURM_NTASKS", "SLURM_NTASKS_PER_NODE", "SLURM_CPUS_ON_NODE",
        "SLURM_CPUS_PER_TASK", "SLURM_MEM_PER_NODE", "SLURM_MEM_PER_CPU",
        "SLURM_SUBMIT_DIR", "SLURM_SUBMIT_HOST", "SLURM_JOB_USER",
        "SLURM_JOB_UID", "SLURM_ARRAY_JOB_ID", "SLURM_ARRAY_TASK_ID",
        "SLURM_LOCALID", "SLURM_PROCID", "SLURM_NODEID",
    ]
    found = False
    for var in slurm_vars:
        val = os.environ.get(var)
        if val:
            print(f"  {var:<30} {val}")
            found = True
    if not found:
        print("  Not running inside a SLURM job.")


def print_cluster_info():
    section("Cluster Info")
    version = _run(["sinfo", "--version"])
    if version is None:
        print("  SLURM not available or sinfo not in PATH.")
        return
    print(f"  SLURM version:  {version}")

    conf = _run(["scontrol", "show", "config"])
    if conf:
        keys = ["ClusterName", "ControlMachine", "ControlAddr",
                "SlurmctldHost", "DefaultPartition", "MaxJobCount",
                "MaxArraySize", "SchedulerType", "SelectType"]
        for line in conf.splitlines():
            for key in keys:
                if line.strip().startswith(key + " "):
                    print(f"  {line.strip()}")
                    break


def print_partitions():
    section("Partitions")
    out = _run([
        "sinfo", "--noheader",
        "-o", "%P %a %l %D %T %C"
    ])
    if out is None:
        print("  sinfo not available.")
        return
    print(f"  {'Partition':<20} {'Avail':<8} {'Time Limit':<14} {'Nodes':<7} {'State':<12} {'CPUs (A/I/O/T)'}")
    print("  " + "-" * 80)
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 6:
            print(f"  {parts[0]:<20} {parts[1]:<8} {parts[2]:<14} {parts[3]:<7} {parts[4]:<12} {parts[5]}")


def print_nodes():
    section("Nodes")
    out = _run([
        "sinfo", "--noheader",
        "-o", "%n %T %c %m %G %f"
    ])
    if out is None:
        print("  sinfo not available.")
        return
    print(f"  {'Node':<20} {'State':<12} {'CPUs':<6} {'Memory (MB)':<14} {'Gres':<20} {'Features'}")
    print("  " + "-" * 90)
    seen = set()
    for line in out.splitlines():
        parts = line.split(None, 5)
        if len(parts) >= 5 and parts[0] not in seen:
            seen.add(parts[0])
            features = parts[5] if len(parts) > 5 else ""
            print(f"  {parts[0]:<20} {parts[1]:<12} {parts[2]:<6} {parts[3]:<14} {parts[4]:<20} {features}")


def print_queue():
    section("Job Queue")
    out = _run([
        "squeue", "--noheader",
        "-o", "%i %j %u %T %M %l %D %R %P"
    ])
    if out is None:
        print("  squeue not available.")
        return

    lines = out.splitlines() if out else []
    if not lines:
        print("  No jobs in queue.")
        return

    # Summary counts by state
    states = {}
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            st = parts[3]
            states[st] = states.get(st, 0) + 1
    print(f"  Total jobs: {len(lines)}")
    for st, count in sorted(states.items()):
        print(f"    {st:<12} {count}")

    print()
    print(f"  {'JobID':<10} {'Name':<20} {'User':<12} {'State':<10} {'Time':<12} {'Limit':<12} {'Nodes':<6} {'Partition':<14} {'Reason'}")
    print("  " + "-" * 105)
    for line in lines[:20]:
        parts = line.split(None, 8)
        if len(parts) >= 8:
            reason = parts[8] if len(parts) > 8 else ""
            print(
                f"  {parts[0]:<10} {parts[1][:19]:<20} {parts[2]:<12} "
                f"{parts[3]:<10} {parts[4]:<12} {parts[5]:<12} "
                f"{parts[6]:<6} {parts[8] if len(parts) > 8 else parts[7]:<14}"
            )


def print_accounting():
    section("Recent Jobs (sacct — last 24h)")
    out = _run([
        "sacct", "--noheader", "--starttime=now-24hours",
        "-o", "JobID,JobName,User,Partition,State,Elapsed,AllocCPUS,ReqMem,NodeList",
        "--parsable2"
    ])
    if out is None:
        print("  sacct not available.")
        return
    lines = out.splitlines() if out else []
    if not lines:
        print("  No jobs found in the last 24 hours.")
        return
    print(f"  {'JobID':<12} {'Name':<20} {'User':<12} {'Partition':<14} {'State':<12} {'Elapsed':<10} {'CPUs':<6} {'ReqMem':<10} {'NodeList'}")
    print("  " + "-" * 105)
    for line in lines[:20]:
        parts = line.split("|")
        if len(parts) >= 9:
            print(
                f"  {parts[0]:<12} {parts[1][:19]:<20} {parts[2]:<12} "
                f"{parts[3]:<14} {parts[4]:<12} {parts[5]:<10} "
                f"{parts[6]:<6} {parts[7]:<10} {parts[8]}"
            )


if __name__ == "__main__":
    print_job_env()
    if _slurm_available():
        print_cluster_info()
        print_partitions()
        print_nodes()
        print_queue()
        print_accounting()
    else:
        print("\n  SLURM commands (sinfo/squeue/sacct) not found in PATH.")
