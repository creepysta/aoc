import sys
import unittest

from copy import deepcopy
from collections import defaultdict
from contextlib import redirect_stdout

def parse(content: str):
    line =  [line.strip() for line in content.split("\n") if len(line.strip()) ][0]
    nums = map(int, line.split(" "))
    return list(nums)


def part1(content: str):
    nums = parse(content)
    rv = nums[:]
    for _ in range(25):
        copy: list[int] = []
        for n in rv:
            ln = len(str(n))
            x, y = None, None
            if n == 0:
                # replace with 1
                x = 1
            elif ln % 2 == 0:
                # split into 2 nums
                x, y = str(n)[0:ln//2], str(n)[ln//2:]
            else:
                x = n * 2024
            if x is not None:
                copy.append(int(x))
            if y is not None:
                copy.append(int(y))

        rv = copy[:]

    # print(rv)
    return len(rv)


def part2(content: str) -> int:

    nums = parse(content)
    cnt: dict[int, int] = defaultdict(int)

    for n in nums:
        cnt[n] += 1

    for step in range(75):
        copy: dict[int, int] = defaultdict(int)
        for n, rep in cnt.items():
            ln = len(str(n))
            if n == 0:
                # replace with 1
                x = 1
                copy[x] += rep
            elif ln % 2 == 0:
                # split into 2 nums
                x, y = str(n)[0:ln//2], str(n)[ln//2:]
                copy[int(x)] += rep
                copy[int(y)] += rep
            else:
                x = n * 2024
                copy[x] += rep

        cnt = deepcopy(copy)

    # print(cnt)
    return sum(cnt.values())


class Testday11(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
        125 17
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 55312)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 65601038650482)



def main():
    inp = open("./in.txt", 'r').read()
    with redirect_stdout(sys.stderr):
        p1 = part1(inp)
        p2 = part2(inp)

    print(f"{p1=}\n{p2=}")

    unittest.main(argv=sys.argv[:1])

    return 0


if __name__ == "__main__":
    main()



