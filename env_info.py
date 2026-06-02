import os
import sys
import subprocess
import sysconfig


def section(title):
    print(f"\n=== {title} ===")


def _run(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return result.stdout.strip() if result.returncode == 0 else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def print_python_env():
    section("Python Environment")
    print(f"  Executable:     {sys.executable}")
    print(f"  Version:        {sys.version}")
    print(f"  Prefix:         {sys.prefix}")
    print(f"  Exec prefix:    {sys.exec_prefix}")
    print(f"  Platform:       {sys.platform}")

    venv = os.environ.get("VIRTUAL_ENV")
    conda = os.environ.get("CONDA_DEFAULT_ENV") or os.environ.get("CONDA_PREFIX")
    if venv:
        print(f"  Virtual env:    {venv}")
    elif conda:
        print(f"  Conda env:      {conda}")
    else:
        print(f"  Virtual env:    None (system Python)")


def print_installed_packages():
    section("Installed Python Packages")
    out = _run([sys.executable, "-m", "pip", "list", "--format=columns"])
    if out is None:
        print("  pip not available.")
        return
    lines = out.splitlines()
    # Print header + all packages
    for line in lines:
        print(f"  {line}")
    print(f"\n  Total: {max(0, len(lines) - 2)} packages")


def print_cuda_env():
    section("CUDA / GPU Environment")
    cuda_vars = [
        "CUDA_HOME", "CUDA_ROOT", "CUDA_PATH", "CUDA_VISIBLE_DEVICES",
        "NVIDIA_VISIBLE_DEVICES", "NVIDIA_DRIVER_CAPABILITIES",
        "LD_LIBRARY_PATH", "CUDNN_PATH", "NCCL_DEBUG",
    ]
    found = False
    for var in cuda_vars:
        val = os.environ.get(var)
        if val:
            display = val if len(val) <= 80 else val[:77] + "..."
            print(f"  {var:<30} {display}")
            found = True
    if not found:
        print("  No CUDA environment variables set.")

    # nvcc version
    nvcc = _run(["nvcc", "--version"])
    if nvcc:
        for line in nvcc.splitlines():
            if "release" in line.lower() or "cuda" in line.lower():
                print(f"  nvcc:           {line.strip()}")
                break


def print_mpi_env():
    section("MPI Environment")
    mpi_vars = [
        "OMPI_COMM_WORLD_SIZE", "OMPI_COMM_WORLD_RANK", "OMPI_COMM_WORLD_LOCAL_RANK",
        "MPI_LOCALRANKID", "MPI_LOCALNRANKS", "PMI_RANK", "PMI_SIZE",
        "PMIX_RANK", "PMIX_NAMESPACE",
    ]
    found = False
    for var in mpi_vars:
        val = os.environ.get(var)
        if val:
            print(f"  {var:<35} {val}")
            found = True
    if not found:
        print("  Not running inside an MPI job.")

    # mpirun/mpiexec version
    for cmd in [["mpirun", "--version"], ["mpiexec", "--version"]]:
        out = _run(cmd)
        if out:
            first = out.splitlines()[0]
            print(f"  {cmd[0]}:         {first}")
            break


def print_shell_env():
    section("Shell & User Environment")
    keys = [
        "USER", "HOME", "SHELL", "TERM", "EDITOR", "VISUAL",
        "MANPATH", "INFOPATH", "TMPDIR", "TMP", "TEMP",
        "XDG_DATA_HOME", "XDG_CONFIG_HOME", "XDG_CACHE_HOME", "XDG_RUNTIME_DIR",
    ]
    for k in keys:
        val = os.environ.get(k)
        if val:
            display = val if len(val) <= 80 else val[:77] + "..."
            print(f"  {k:<25} {display}")


def print_path():
    section("PATH Entries")
    path = os.environ.get("PATH", "")
    entries = path.split(os.pathsep)
    for i, entry in enumerate(entries, 1):
        exists = "  " if os.path.isdir(entry) else "! "
        print(f"  {exists}{i:>3}  {entry}")
    print(f"\n  Total: {len(entries)} entries  (! = directory not found)")


def print_sysconfig():
    section("Python sysconfig Paths")
    paths = sysconfig.get_paths()
    for name, path in sorted(paths.items()):
        print(f"  {name:<20} {path}")


if __name__ == "__main__":
    print_python_env()
    print_installed_packages()
    print_cuda_env()
    print_mpi_env()
    print_shell_env()
    print_path()
    print_sysconfig()
