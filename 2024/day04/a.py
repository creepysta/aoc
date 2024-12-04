import sys
from collections import defaultdict
import unittest

def parse(content: str):
    return [list(line) for line in content.split("\n") if len(line) ]


def part1(content: str):
    grid = parse(content)
    xs = [
        (i, j)
        for i, line in enumerate(grid)
        for j, ch in enumerate(line) if ch == 'X'
    ]

    N, M = len(grid), len(grid[0])
    vis = [ [False for _ in line] for line in grid]

    def is_valid(i: int, j: int) -> bool:
        return 0 <= i < N and 0 <= j < M and vis[i][j] == False

    def get_dir_pts(i: int, j: int):
        rv: list[tuple[int, int]] = []
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue

                di, dj = i + y, j + x
                if is_valid(di, dj):
                    rv.append((di, dj))

        return rv

    to_look = ['X', 'M', 'A', 'S']

    # over counts (we only need to look for in one direction
    def bfs(i: int, j: int) -> int:
        lvl = 0
        vis: dict[int, dict[int, bool]] = defaultdict(dict)
        q: list[tuple[int, int]] = []
        q.append((i, j))
        vis[i][j] = True
        c = 0
        nodes = len(q)
        while len(q):
            # breakpoint()
            y, x = q.pop(0)
            for (dy, dx) in get_dir_pts(y, x):
                if all([
                    # lvl < len(to_look),
                    grid[dy][dx] == to_look[lvl+1],
                    not vis[dy].get(dx),
                ]):
                    q.append((dy, dx))
                    vis[dy][dx] = True

            nodes -= 1
            if nodes <= 0:
                # breakpoint()
                nodes = len(q)
                lvl += 1
                if lvl == len(to_look) - 1:
                    c = nodes
                    print(f"{i},{j}={c} | {q=}")
                    break


        return c

    # c = 0
    # for (i, j) in xs:
    #     # breakpoint()
    #     c += bfs(i, j)

    def get_dir(i: int, j: int):
        rv: list[tuple[int, int]] = []
        return [ (y, x) for y in [-1, 0, 1] for x in [-1, 0, 1] if x or y ]

    def check_count(row, col, dy, dx):
        for i, ch in enumerate(to_look):
            py, px = row + i * dy, col + i * dx
            if not is_valid(py, px) or grid[py][px] != ch:
                return 0

        return 1

    c = 0
    for row in range(N):
        for col in range(M):
            for dy, dx in get_dir(row, col):
                c += check_count(row, col, dy, dx)

    return c


def part2(content: str) -> int:
    grid = parse(content)
    N, M = len(grid), len(grid[0])

    def is_valid(i: int, j: int) -> bool:
        return 0 <= i < N and 0 <= j < M

    def check_count(row, col):
        pdiag = [
            (row-1,col-1),
            (row, col),
            (row+1,col+1),
        ]
        odiag = [
            (row-1, col+1),
            (row, col),
            (row+1, col-1),
        ]

        pstr, ostr = None, None
        if all([is_valid(y,x) for y, x in pdiag]):
            pstr = ''.join([ grid[i][j] for i, j in pdiag])

        if all([is_valid(y,x) for y, x in odiag]):
            ostr = ''.join([ grid[i][j] for i, j in odiag])

        checks = {'MAS', 'SAM'}
        pcheck = pstr in checks
        ocheck = ostr in checks

        return 1 if pcheck and ocheck else 0

    c = 0
    for row in range(N):
        for col in range(M):
            c += check_count(row, col)

    return c


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

        return super().setUp()

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 18)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 9)



def main():
    inp = open("./in.txt", 'r').read()
    p1 = part1(inp)
    p2 = part2(inp)
    print(f"{p1=}\n{p2=}")

    unittest.main()
    return 0


if __name__ == "__main__":
    main()


