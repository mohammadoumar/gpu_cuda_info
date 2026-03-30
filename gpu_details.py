import subprocess
import sys


def print_nvidia_smi():
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,driver_version,memory.total,memory.free,memory.used,temperature.gpu,utilization.gpu,utilization.memory",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, check=True
        )
        headers = ["Name", "Driver Version", "Total Memory (MiB)", "Free Memory (MiB)",
                   "Used Memory (MiB)", "Temperature (C)", "GPU Util (%)", "Mem Util (%)"]
        print("=== GPU Details (nvidia-smi) ===")
        for i, line in enumerate(result.stdout.strip().split("\n")):
            values = [v.strip() for v in line.split(",")]
            print(f"\n  GPU {i}:")
            for header, value in zip(headers, values):
                print(f"    {header}: {value}")
    except FileNotFoundError:
        print("nvidia-smi not found.")
    except subprocess.CalledProcessError as e:
        print(f"nvidia-smi error: {e.stderr.strip()}")


def print_torch_info():
    try:
        import torch
        print("\n=== PyTorch GPU Info ===")
        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(i)
                print(f"\n  GPU {i}: {props.name}")
                print(f"    Total Memory:    {props.total_memory / 1024**3:.2f} GB")
                print(f"    Multi-Processors: {props.multi_processor_count}")
                print(f"    CUDA Capability:  {props.major}.{props.minor}")
                alloc = torch.cuda.memory_allocated(i) / 1024**2
                reserved = torch.cuda.memory_reserved(i) / 1024**2
                print(f"    Allocated Memory: {alloc:.1f} MiB")
                print(f"    Reserved Memory:  {reserved:.1f} MiB")
        else:
            print("  CUDA not available.")
    except ImportError:
        print("\nPyTorch not installed — skipping torch info.")


def print_rocm_info():
    try:
        result = subprocess.run(["rocm-smi", "--showproductname", "--showmeminfo", "vram"],
                                capture_output=True, text=True, check=True)
        print("\n=== ROCm GPU Info ===")
        print(result.stdout.strip())
    except FileNotFoundError:
        pass  # Not an AMD system, skip silently


if __name__ == "__main__":
    print_nvidia_smi()
    print_torch_info()
    print_rocm_info()
