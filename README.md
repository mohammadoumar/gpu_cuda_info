# GPU CUDA Info

A small Python script to print GPU details using `nvidia-smi` and PyTorch.

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
```
