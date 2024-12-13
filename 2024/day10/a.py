import sys
import unittest

from copy import deepcopy
from contextlib import redirect_stdout

def parse(content: str):
    lines = [line.strip() for line in content.split("\n") if len(line.strip()) ]
    rv = [[int(x) for x in row] for row in lines]
    return rv


def part1(content: str):
    grid = parse(content)
    zeros = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 0]
    dirs: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    N, M = len(grid), len(grid[0])

    def bfs(sy: int, sx: int):
        q = [(sy, sx)]
        vis = [[False for _ in row] for row in grid]
        vis[sy][sx] = True
        ends = 0
        while len(q):
            vy, vx = q.pop(0)
            for dy, dx in dirs:
                ny, nx = vy + dy, vx + dx
                if (
                    0 <= ny < N
                    and 0 <= nx < M
                    and not vis[ny][nx]
                    and grid[ny][nx] - grid[vy][vx] == 1
                ):
                    if grid[ny][nx] == 9:
                        ends += 1

                    q.append((ny, nx))
                    vis[ny][nx] = True

        return ends

    s = 0
    for sy, sx in zeros:
        s += bfs(sy, sx)

    return s


def part2(content: str) -> int:
    grid = parse(content)
    zeros = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 0]
    dirs: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    N, M = len(grid), len(grid[0])

    def bfs(sy: int, sx: int):
        q = [(sy, sx)]
        vis = [[False for _ in row] for row in grid]
        vis[sy][sx] = True
        ends = 0
        while len(q):
            vy, vx = q.pop(0)
            if grid[vy][vx] == 9:
                ends += 1

            for dy, dx in dirs:
                ny, nx = vy + dy, vx + dx
                if (
                    0 <= ny < N
                    and 0 <= nx < M
                    # and not vis[ny][nx] # allow visiting already visited cells
                    and grid[ny][nx] - grid[vy][vx] == 1
                ):
                    q.append((ny, nx))
                    vis[ny][nx] = True

        return ends

    s = 0
    for sy, sx in zeros:
        s += bfs(sy, sx)

    return s


class Testday10(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
            89010123
            78121874
            87430965
            96549874
            45678903
            32019012
            01329801
            10456732
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 36)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 81)



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



