import sys
import unittest
import re
from math import ceil

from contextlib import redirect_stdout

def parse(content: str):
    lines = [line.strip() for line in content.split("\n") if len(line.strip()) ]
    def parse_(line: str):
        nums_reg = r'(([+-]?\d+),([+-]?\d+))'
        matches = re.findall(nums_reg, line)
        req = [x[0] for x in matches]
        conv: list[list[tuple[int, int]]] = [ tuple([int(y) for y in x.split(",")]) for x in req]  # type: ignore
        return conv

    return [parse_(line) for line in lines]


class Point(tuple):
    def __add__(self, other: tuple):
        return Point([x + y for x, y in zip(self, other)])

    def __mul__(self, other: int):  # type: ignore
        return Point(x * other for x in self)

    def __mod__(self, other: tuple):
        return Point(x % y  for x, y in zip(self, other))


def part1(content: str, DIM: tuple[int, int]):
    W, H = DIM
    points = parse(content)
    grid = [ [0 for _ in range(W)] for _ in range(H) ]
    for (pos, vel) in points:
        pos_, vel_ = Point(pos), Point(vel)
        x, y = (pos_ + vel_ * 100) % (W, H)
        grid[y][x] += 1


    def calc(grid: list[list[int]]):
        splits = [[], []]
        for row in grid:
            splits[0].append(row[:W//2])
            splits[1].append(row[ceil(W/2):])


        s1 = sum(sum(x) for x in splits[0])
        s2 = sum(sum(x) for x in splits[1])

        return s1 * s2

    ans = 1
    for gd in [grid[:H//2], grid[ceil(H/2):]]:
        ans *= calc(gd)

    return ans


def show(grid: list[list[int]], rep: int):
    final: list[str] = []
    ok = False
    for row in grid:
        st = ''.join(map(str, row))
        final.append(st)
        ok = ok or '1'*10 in st

    if not ok:
        return False

    # STUPID
    print(rep)
    print('\n'.join(final))
    print("")
    print("")
    return True


def part2(content: str, DIM: tuple[int, int]) -> int:
    W, H = DIM
    points = parse(content)

    def move_points(mag: int, grid: list[list[int]]):
        for (pos, vel) in points:
            pos_, vel_ = Point(pos), Point(vel)
            x, y = (pos_ + vel_ * mag) % (W, H)
            grid[y][x] += 1

    time_lapsed = 0
    while True:
        print(f"{time_lapsed=}")
        grid = [ [0 for _ in range(W)] for _ in range(H) ]
        move_points(time_lapsed, grid)
        ok = show(grid, time_lapsed)
        if ok:
            break

        time_lapsed += 1

    return time_lapsed


class Testday14(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
            p=0,4 v=3,-3
            p=6,3 v=-1,-3
            p=10,3 v=-1,2
            p=2,0 v=2,-1
            p=0,0 v=1,3
            p=3,0 v=-2,-2
            p=7,6 v=-1,-3
            p=3,0 v=-1,-2
            p=9,3 v=2,3
            p=7,3 v=-1,2
            p=2,4 v=2,-3
            p=9,5 v=-3,-3
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input, (11, 7))
        self.assertEqual(got, 12)

    # def test_part_2(self):
    #     got = part2(self.input)
    #     self.assertEqual(got, -9999999)



def main():
    inp = open("./in.txt", 'r').read()
    with redirect_stdout(sys.stderr):
        p1 = part1(inp, (101, 103))
        p2 = part2(inp, (101, 103))

    print(f"{p1=}\n{p2=}")

    unittest.main(argv=sys.argv[:1])

    return 0


if __name__ == "__main__":
    main()



