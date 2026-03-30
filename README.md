# GPU CUDA Info

Two Python scripts to print GPU and node details.

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
