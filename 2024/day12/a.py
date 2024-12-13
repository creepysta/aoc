import sys
import unittest

from contextlib import redirect_stdout

def parse(content: str):
    return [list(line.strip()) for line in content.split("\n") if len(line.strip()) ]

def part1(content: str):
    grid = parse(content)
    N, M = len(grid), len(grid[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vis = [[False for _ in row] for row in grid]

    def is_valid(y: int, x: int):
        return 0 <= y < N and 0 <= x < M

    def bfs(ch: str, sy: int, sx: int):
        q = [(sy, sx)]
        vis[sy][sx] = True

        area, peri = 0, 0
        while len(q):
            y, x = q.pop(0)
            area += 1
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if (
                    is_valid(ny, nx)
                    and vis[ny][nx] == False
                    and ch == grid[ny][nx]
                ):
                    q.append((ny, nx))
                    vis[ny][nx] = True

                if (
                    not is_valid(ny, nx)
                    or ch != grid[ny][nx]
                ):
                    peri += 1

        return area, peri

    rv = 0
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if vis[y][x]:
                continue

            area, peri = bfs(ch, y, x)
            rv += area * peri
            # print(f"{ch=}, {y=}, {x=}, {area=}, {peri=}")

    return rv


class List(list):
    def __getitem__(self, k):
        if k < 0 or k >= len(self):
            return List()

        return list.__getitem__(self, k)


def part2(content: str) -> int:
    grid = List([List(row) for row in parse(content)])
    N, M = len(grid), len(grid[0])

    vis = [[False for _ in row] for row in grid]

    def is_valid(y: int, x: int):
        return 0 <= y < N and 0 <= x < M

    def dfs(ch: str, y: int, x: int):
        area, sides = 0, 0
        def recur(y, x):
            nonlocal area, sides

            if (
                not is_valid(y, x)
                or vis[y][x]
                or grid[y][x] != ch
            ):
                return

            vis[y][x] = True
            area += 1

            sides += grid[y-1][x] != ch and (grid[y-1][x-1] == ch or grid[y][x-1] != ch);
            sides += grid[y][x+1] != ch and (grid[y+1][x+1] == ch or grid[y+1][x] != ch);
            sides += grid[y+1][x] != ch and (grid[y+1][x+1] == ch or grid[y][x+1] != ch);
            sides += grid[y][x-1] != ch and (grid[y-1][x-1] == ch or grid[y-1][x] != ch);

            recur(y-1, x);
            recur(y, x+1);
            recur(y+1, x);
            recur(y, x-1);

        recur(y, x)
        return area, sides

    rv = 0
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if vis[y][x]:
                continue

            area, sides = dfs(ch, y, x)
            rv += area * sides
            # print(f"{ch=}, {y=}, {x=}, {area=}, {sides=}")

    return rv


class Testday12(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
            RRRRIICCFF
            RRRRIICCCF
            VVRRRCCFFF
            VVRCCCJFFF
            VVVVCJJCFE
            VVIVCCJJEE
            VVIIICJJEE
            MIIIIIJJEE
            MIIISIJEEE
            MMMISSJEEE
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 1930)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 1206)



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



