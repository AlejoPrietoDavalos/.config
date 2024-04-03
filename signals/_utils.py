from typing import Callable
from pathlib import Path
import signal
import time
import os

def get_path_config_tmp() -> Path:
    return Path.home() / ".config" / "tmp"

def get_path_pid(path_config_tmp: Path, _file_: str) -> Path:
    path_pid = path_config_tmp / os.path.basename(_file_)
    path_pid = path_pid.with_suffix(".pid")
    print(path_pid)
    return path_pid

def create_pid_file(path_config_tmp: Path, _file_: str) -> None:
    path_pid = get_path_pid(path_config_tmp, _file_)
    with open(path_pid, "w") as f:
        pid = str(os.getpid())
        print(f"Save PID - SIGUSR1: {pid} | {path_pid.name}")
        f.write(pid)

def start_signal(fn_main: Callable, path_config_tmp: Path, _file_: str) -> None:
    path_config_tmp = get_path_config_tmp()
    create_pid_file(path_config_tmp, _file_)
    signal.signal(signal.SIGUSR1, fn_main)
    while True:
        time.sleep(60)