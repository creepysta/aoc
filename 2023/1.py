import sys
from utils import lines


def one():
    def get_val(line: str) -> int | None:
        for ch in line:
            if ch.isdigit():
                return int(ch)

        return None

    ans = 0
    ls = lines("1.in1")
    for line in ls:
        left = get_val(line)
        rline = line[::-1]
        right = get_val(rline)
        if not (left is None or  right is None):
            val = 10*left + right
            ans += val

    print("One: ", ans)


def two():
    num_map = {
        'one': 'one1one', 'two': 'two2two', 'three': 'three3three',
        'four': 'four4four', 'five': 'five5five', 'six': 'six6six',
        'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'
    }
    preped_lines = []
    for line in lines("1.in2"):
        l = line
        for k, v in num_map.items():
            l = l.replace(k, v)

        preped_lines.append(l)

    def get_val(line: str) -> int | None:
        for ch in line:
            if ch.isdigit():
                return int(ch)

        return None

    ans = 0
    for line in preped_lines:
        left = get_val(line)
        rline = line[::-1]
        right = get_val(rline)
        if not (left is None or  right is None):
            val = 10*left + right
            ans += val

    print("Two: ", ans)


one()
two()
