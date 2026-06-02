# GPU CUDA Info

Four Python scripts to print GPU, node, OS, and CPU details.

## Sample Output

### nvidia-smi

| Property | Value |
|---|---|
| Name | NVIDIA GeForce RTX 2080 Ti |
| Driver Version | 550.54.14 |
| Total Memory | 11264 MiB |
| Free Memory | 8280 MiB |
| Used Memory | 2723 MiB |
| Temperature | 38°C |
| GPU Utilization | 0% |
| Memory Utilization | 0% |

### PyTorch

| Property | Value |
|---|---|
| Name | NVIDIA GeForce RTX 2080 Ti |
| Total Memory | 10.75 GB |
| Multi-Processors | 68 |
| CUDA Capability | 7.5 |
| Allocated Memory | 0.0 MiB |
| Reserved Memory | 0.0 MiB |

## Usage

```bash
python3 gpu_details.py
python3 node_info.py
python3 os_info.py
python3 cpu_details.py
```

---

## Node Info (`node_info.py`)

### Node Identity

| Property | Value |
|---|---|
| Hostname | l3icalcul01 |
| FQDN | l3icalcul01.univ-lr.fr |
| OS | Linux 6.1.0-20-amd64 |
| OS Version | Debian 6.1.85-1 (2024-04-11) |
| Architecture | x86_64 |
| Python | 3.11.2 |

### CPU

| Property | Value |
|---|---|
| Physical Cores | 14 |
| Logical Cores | 28 |
| Max Frequency | 4643 MHz |
| Current Frequency | 1218 MHz |
| CPU Usage | 1.1% |
| Load Avg (1/5/15 min) | 0.45 / 0.39 / 0.25 |

### Memory

| Property | Value |
|---|---|
| Total RAM | 125.47 GB |
| Available RAM | 114.82 GB |
| Used RAM | 10.66 GB (8.5%) |
| Swap Total | 0.95 GB |
| Swap Used | 0.05 GB (5.7%) |

### Disk

| Mount | Filesystem | Total | Used |
|---|---|---|---|
| / | ext4 | 1831.3 GB | 85.3 GB (4.9%) |
| /boot/efi | vfat | 0.5 GB | 0.0 GB (1.1%) |

### Network Interfaces

| Interface | Status | IP |
|---|---|---|
| lo | UP | 127.0.0.1 |
| enp2s0 | DOWN | 192.168.0.101 |
| eno1 | UP | 10.4.33.40 |

### SLURM Environment

| Variable | Value |
|---|---|
| SLURM_JOB_ID | 396743 |

---

## OS Info (`os_info.py`)

### OS Identity

| Property | Value |
|---|---|
| System | Linux |
| Release | 6.1.0-20-amd64 |
| Version | #1 SMP PREEMPT_DYNAMIC Debian 6.1.85-1 (2024-04-11) |
| Platform | Linux-6.1.0-20-amd64-x86_64-with-glibc2.36 |
| Architecture | x86_64 / 64bit |
| Distro | Debian GNU/Linux 12 (bookworm) |
| Distro ID | debian |
| Distro Version | 12 |

### Kernel

| Property | Value |
|---|---|
| Kernel Release | 6.1.0-20-amd64 |
| Kernel Version | #1 SMP PREEMPT_DYNAMIC Debian 6.1.85-1 (2024-04-11) |

### Uptime & Boot

| Property | Value |
|---|---|
| Boot Time | 2025-06-24 11:23:33 |
| Uptime | 343d 9h 20m |

### Python Runtime

| Property | Value |
|---|---|
| Version | 3.11.2 |
| Implementation | CPython |
| Executable | /usr/bin/python3 |
| Prefix | /usr |

### Locale & Timezone

| Property | Value |
|---|---|
| Timezone | CEST |
| LANG | fr_FR.UTF-8 |

### Key Environment Variables

| Variable | Value |
|---|---|
| HOME | /Utilisateurs/umushtaq |
| USER | umushtaq |
| SHELL | /bin/bash |

---

## CPU Details (`cpu_details.py`)

Outputs JSON with combined CPU and OS information.

### CPU

| Property | Value |
|---|---|
| Model | AMD EPYC 7513 32-Core Processor |
| Vendor | AuthenticAMD |
| Physical Cores | 64 |
| Logical Cores | 64 |
| Max Frequency | 2600.0 MHz |
| Min Frequency | 1500.0 MHz |
| Current Frequency | 2086.32 MHz |

### OS

| Property | Value |
|---|---|
| System | Linux |
| Node | l3icalculmaster |
| Release | 6.1.0-20-amd64 |
| Version | #1 SMP PREEMPT_DYNAMIC Debian 6.1.85-1 (2024-04-11) |
| Platform | Linux-6.1.0-20-amd64-x86_64-with-glibc2.36 |
| Architecture | 64bit / ELF |
| Python Version | 3.11.2 |
