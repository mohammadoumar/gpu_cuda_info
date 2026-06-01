"""Get CPU and OS information.

Provides a simple cross-platform function `get_system_info()` that returns a
dictionary with CPU and OS details. Uses psutil when available for richer CPU
information and falls back to stdlib methods.
"""
from __future__ import annotations

import platform
import sys
import os
import multiprocessing
from typing import Dict, Any

try:
    import psutil
except Exception:
    psutil = None


def _cpu_info() -> Dict[str, Any]:
    info: Dict[str, Any] = {}

    # Basic info from stdlib
    info['physical_cores'] = getattr(multiprocessing, 'cpu_count')() if hasattr(multiprocessing, 'cpu_count') else None
    # logical cores: prefer psutil if available
    try:
        info['logical_cores'] = psutil.cpu_count(logical=True) if psutil else os.cpu_count()
    except Exception:
        info['logical_cores'] = os.cpu_count()

    # CPU frequency and usage if psutil is available
    if psutil:
        try:
            freq = psutil.cpu_freq()
            if freq:
                info['max_frequency_mhz'] = round(freq.max, 2) if freq.max else None
                info['min_frequency_mhz'] = round(freq.min, 2) if freq.min else None
                info['current_frequency_mhz'] = round(freq.current, 2) if freq.current else None
        except Exception:
            pass
        try:
            info['cpu_percent_per_cpu'] = psutil.cpu_percent(interval=0.1, percpu=True)
        except Exception:
            pass

    # Try to glean additional vendor/model info from platform or /proc
    info['processor'] = platform.processor() or None
    info['machine'] = platform.machine() or None

    # On Linux, try reading /proc/cpuinfo for model name
    if sys.platform.startswith('linux'):
        try:
            with open('/proc/cpuinfo', 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if ':' in line:
                        key, val = [p.strip() for p in line.split(':', 1)]
                        if key.lower() in ('model name', 'vendor_id') and key.lower() not in info:
                            info[key.lower().replace(' ', '_')] = val
                            # break when we have model name
                            if 'model name' in info:
                                break
        except Exception:
            pass

    return info


def _os_info() -> Dict[str, Any]:
    return {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'platform': platform.platform(),
        'architecture': platform.architecture(),
        'python_version': platform.python_version(),
    }


def get_system_info() -> Dict[str, Any]:
    """Return combined CPU and OS information as a dictionary."""
    return {
        'cpu': _cpu_info(),
        'os': _os_info(),
    }


def main() -> None:
    """Print system info to stdout in a readable form."""
    import json

    info = get_system_info()
    print(json.dumps(info, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
