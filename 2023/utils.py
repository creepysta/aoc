from functools import wraps
import time


def lines(fpath: str) -> list[str]:
    with open(fpath, 'r') as f:
        return [line.strip("\r\n ") for line in f]


def bench(func):
    @wraps(func)
    def inner(*args, **kwargs):
        prev = time.perf_counter_ns()
        func(*args, **kwargs)
        now = time.perf_counter_ns()
        print(f"[{func.__qualname__}] Time taken: {(now - prev) / 1e9}s")

    return inner
