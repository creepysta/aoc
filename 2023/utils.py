from argparse import ArgumentParser
import requests
from functools import wraps
import time


def lines(fpath: str) -> list[str]:
    with open(fpath, 'r') as f:
        return [line.strip("\r\n ") for line in f]


def bench(func):
    @wraps(func)
    def inner(*args, **kwargs):
        prev = time.perf_counter_ns()
        rv = func(*args, **kwargs)
        now = time.perf_counter_ns()
        vargs = ",".join([f"{x!r}" for x in args])
        vkwargs = ",".join([f"{k}={v!r}" for k, v in kwargs.items()])
        fargs = ",".join(filter(lambda x: x.strip(), [vargs, vkwargs]))
        print(f"[{func.__qualname__}({fargs})] Time taken: {(now - prev) / 1e9}s")
        return rv

    return inner


def get_token():
    with open(".env", 'r') as f:
        token = f.read().split('=')[1].strip(' \n')

    return token


def setup(day: str):
    print(f"Setting up {day=}...")
    print(f"Creating scratch {day}.py")
    with open(f"template.py", 'r') as temp, open(f"{day}.py", 'w') as f:
        f.write(temp.read().replace('{day}', day))

    print(f"Fetching test input in {day}.in1...")
    token = get_token()
    res = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input",
        cookies={'session': token}
    )
    res.raise_for_status()
    with open(f"{day}.in1", 'w') as f:
        f.write(res.text)

def submit(day: str, ans: int):
    token = get_token()
    print(f"Submitting ans for {day}...")
    res = requests.post(
        f"https://adventofcode.com/2023/day/{day}/answer",
        cookies={'session': token},
        json={"answer": ans},
    )
    res.raise_for_status()
    print("Answer response: ", res.text)


def main():
    parser = ArgumentParser()
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('--submit', action='store_true')
    parser.add_argument('--day')
    parser.add_argument('--ans', type=int)
    args = parser.parse_args()
    if args.setup:
        assert args.day and len(args.day) > 0
        setup(args.day)

    if args.submit:
        submit(args.day, args.ans)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())


