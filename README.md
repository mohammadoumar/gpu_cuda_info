# GPU CUDA Info

Seven Python scripts to print GPU, node, OS, CPU, network, memory, and disk details.

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
python3 network_info.py
python3 memory_info.py
python3 disk_info.py
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

---

## Network Info (`network_info.py`)

### Hostname

| Property | Value |
|---|---|
| Hostname | l3icalculmaster |
| FQDN | l3icalculmaster.univ-lr.fr |
| Primary IP | 10.4.130.6 |

### Network Interfaces

| Interface | Status | Speed | MTU | IPv4 | MAC |
|---|---|---|---|---|---|
| enp67s0f0 | UP | 1000 Mbps | 1500 | 10.4.130.6/255.255.0.0 | 3c:ec:ef:f9:95:e8 |
| enp67s0f1 | UP | 1000 Mbps | 1500 | 192.168.0.1/255.255.255.0 | 3c:ec:ef:f9:95:e9 |
| lo | UP | N/A | 65536 | 127.0.0.1/255.0.0.0 | 00:00:00:00:00:00 |

### Network I/O Counters

| Interface | Bytes Sent | Bytes Recv | Pkts Sent | Pkts Recv | Errs In | Errs Out |
|---|---|---|---|---|---|---|
| enp67s0f0 | 3,775,527,741,641 | 6,758,471,169,048 | 4,401,557,168 | 6,012,594,859 | 18666 | 0 |
| enp67s0f1 | 25,962,780,236,127 | 31,616,089,289,454 | 37,548,240,716 | 38,615,203,382 | 0 | 0 |
| lo | 1,406,378,783,656 | 1,406,378,783,656 | 1,561,856,982 | 1,561,856,982 | 0 | 0 |

### Active TCP Connections

| Property | Value |
|---|---|
| Established | 74 |
| Listening | 79 |

#### Listening Ports (sample)

| Local Address | PID |
|---|---|
| 0.0.0.0:22 | N/A |
| 0.0.0.0:25 | N/A |
| 0.0.0.0:80 | N/A |
| 127.0.0.1:3306 | N/A |
| 0.0.0.0:6817 | N/A |

---

## Memory Info (`memory_info.py`)

### Virtual Memory (RAM)

| Property | Value |
|---|---|
| Total | 251.55 GB |
| Available | 221.08 GB |
| Used | 30.48 GB (12.1%) |
| Free | 7.73 GB |
| Cached | 214.94 GB |
| Buffers | 0.62 GB |
| Shared | 0.02 GB |

### Swap Memory

| Property | Value |
|---|---|
| Total | 0.95 GB |
| Used | 0.95 GB (100.0%) |
| Free | 0.00 GB |
| Swapped In | 0.61 GB |
| Swapped Out | 2.81 GB |

### Kernel Memory Breakdown (/proc/meminfo)

| Field | Value (GB) |
|---|---|
| MemTotal | 251.55 GB |
| MemAvailable | 221.08 GB |
| Active | 93.39 GB |
| Inactive | 120.89 GB |
| AnonPages | 23.49 GB |
| Cached | 189.74 GB |
| Slab | 28.07 GB |
| KReclaimable | 25.21 GB |

### Top 10 Processes by Memory Usage

| PID | Name | RSS | VMS | Mem% |
|---|---|---|---|---|
| 1707904 | remote-dev-server | 3.78 GB | 8.16 GB | 1.50% |
| 498154 | mariadbd | 3.25 GB | 125.85 GB | 1.29% |
| 4181861 | node | 2.58 GB | 13.60 GB | 1.03% |
| 1148739 | slurmctld | 1.01 GB | 25.71 GB | 0.40% |
| 2774158 | node | 0.91 GB | 23.99 GB | 0.36% |

---

## Disk Info (`disk_info.py`)

### Disk Partitions & Usage

| Mountpoint | Device | Filesystem | Total | Used | Free |
|---|---|---|---|---|---|
| / | /dev/nvme0n1p2 | ext4 | 3518.32 GB | 89.77 GB (2.7%) | 3249.76 GB |
| /boot/efi | /dev/nvme0n1p1 | vfat | 0.50 GB | 0.01 GB (1.1%) | 0.49 GB |

### Disk I/O Counters

| Device | Reads | Writes | Read Bytes | Write Bytes | Read Time | Write Time |
|---|---|---|---|---|---|---|
| nvme0n1 | 8,890,160 | 79,415,909 | 537.75 GB | 1522.88 GB | 901118 ms | 15558411 ms |
| nvme0n1p2 | 8,861,917 | 79,325,671 | 537.10 GB | 1520.08 GB | 899120 ms | 15544763 ms |
| nvme0n1p3 | 26,813 | 90,236 | 0.61 GB | 2.81 GB | 1559 ms | 13648 ms |

### Block Devices (lsblk)

| Name | Size | Type | Filesystem | Mountpoint | Model | Rotational |
|---|---|---|---|---|---|---|
| sda | 7T | disk | | | KINGSTON SEDC600M7680G | No |
| sdb | 7T | disk | | | KINGSTON SEDC450R7680G | No |
| nvme0n1 | 3.5T | disk | | | SAMSUNG MZQL23T8HCLS | No |
| nvme0n1p1 | 512M | part | vfat | /boot/efi | | No |
| nvme0n1p2 | 3.5T | part | ext4 | / | | No |
| nvme0n1p3 | 977M | part | swap | [SWAP] | | No |

### Inode Usage

| Mountpoint | Total Inodes | Used | Free | Use% |
|---|---|---|---|---|
| / | 234,332,160 | 609,653 | 233,722,507 | 0.3% |
| /boot/efi | 0 | 0 | 0 | 0.0% |
