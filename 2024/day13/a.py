import sys
from math import gcd
import unittest
import re

from contextlib import redirect_stdout

def parse(content: str, more=False):
    blocks = [block for block in content.split("\n\n") if len(block.strip()) ]
    def parse_(line: str):
        line = line.strip()
        match_reg = r'=?([+-]?\d+)'
        splits = line.split(":")
        rs = splits[1]
        l = re.findall(match_reg, rs)
        a, b = list(map(int, l))
        if more and line.startswith("Prize"):
            const = 10_000_000_000_000
            return (a + const, b + const)

        return (a, b)

    return [[ parse_(line) for line in block.split("\n") if len(line.strip()) ] for block in blocks]

OpType = tuple[int, int]

def part1(content: str):
    games = parse(content)

    def solve(oa: OpType, ob: OpType, rs: OpType) -> int:
        """
        | x1, y1 ||a|   |x|
        | x2, y2 ||b| = |y|
        """
        xa, ya = oa
        xb, yb = ob
        xx, yy = rs
        for ca in range(100):
            cax, cay = ca * xa, ca * ya
            for cb in range(100):
                cbx, cby = cb * xb, cb * yb

                if cax + cbx == xx and cay + cby == yy:
                    return 3*ca + 1*cb  # 3 tokens for btn a and 1 for btn b
        return 0

    ans = 0
    for game in games:
        ba, bb, p = game
        ans += solve(ba, bb, p)

    return ans


def part2(content: str) -> int:
    games = parse(content, more=True)

    def solve(oa: OpType, ob: OpType, rs: OpType) -> int:
        xa, ya = oa
        xb, yb = ob
        xx, yy = rs
        """
        xa * A + xb * B = xx
        ya * A + yb * B = yy

        solve for B:
        ya * xa * A + ya * xb * B = ya * xx
        xa * ya * A + xa * yb * B = xa * yy

        B = ((ya * xx) - (xa * yy)) / ((ya * xb) - (xa * yb))
        A = (xx - xb * B) / xa

        """
        B, rb = divmod((ya * xx) - (xa * yy), (ya * xb) - (xa * yb))
        A, ra = divmod(xx - (xb * B), xa)

        if ra or rb:
            return 0

        return 3 * A + B


    ans = 0
    for game in games:
        ba, bb, p = game
        ans += solve(ba, bb, p)

    return ans


class Testday13(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """

            Button A: X+94, Y+34
            Button B: X+22, Y+67
            Prize: X=8400, Y=5400

            Button A: X+26, Y+66
            Button B: X+67, Y+21
            Prize: X=12748, Y=12176

            Button A: X+17, Y+86
            Button B: X+84, Y+37
            Prize: X=7870, Y=6450

            Button A: X+69, Y+23
            Button B: X+27, Y+71
            Prize: X=18641, Y=10279

        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 480)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 875318608908)



def main():
    inp = open("./in.txt", 'r').read()
    with redirect_stdout(None):
        p1 = part1(inp)
        p2 = part2(inp)

    print(f"{p1=}\n{p2=}")

    unittest.main(argv=sys.argv[:1])

    return 0


if __name__ == "__main__":
    main()



