import sys
import unittest
from contextlib import redirect_stdout


def parse(content: str):
    return [list(line.strip()) for line in content.split("\n") if len(line.strip()) ]

def turn_right(dy: int, dx: int):
    # https://en.wikipedia.org/wiki/Rotation_matrix
    # clockwise (-theta)
    # x2 = xcos90 - ysin90  = dy
    # y2 = xsin90 + ycos90 = -dx
    x2 = -dy
    y2 = dx
    return y2, x2

def part1(content: str):
    grid = parse(content)
    pos = [(i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch == '^' ][0]
    grid[pos[0]][pos[1]] = '.'

    def is_valid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    vis = [[0 for _ in row] for row in grid]

    def cont(y: int, x: int, dy: int, dx: int) -> tuple[bool, tuple[int, int], int]:
        c, i = 0, 1
        while True:
            ny, nx = y + i*dy, x + i*dx
            py, px = y + (i-1)*dy, x + (i-1)*dx
            if not is_valid(ny, nx):
                return False, (ny, nx), c

            vis[py][px] += 1
            if grid[ny][nx] == '#':
                return True, (py, px), c

            c+=1
            i+=1

    cdir = (-1, 0) # go up
    cpos = pos
    while True:
        more, (ny, nx), cnt = cont(*cpos, *cdir)
        cdir = turn_right(*cdir)
        cpos = (ny, nx)
        if not more:
            break

    c = sum([e > 0 for row in vis for e in row])

    return c+1


def part2(content: str) -> int:
    grid = parse(content)
    pos = [(i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch == '^' ][0]
    start_me = pos
    grid[pos[0]][pos[1]] = '.'

    def is_valid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    vis_pts = [[0 for _ in row] for row in grid]

    def cont(y: int, x: int, dy: int, dx: int) -> tuple[bool, tuple[int, int], int]:
        c, i = 0, 1
        while True:
            ny, nx = y + i*dy, x + i*dx
            py, px = y + (i-1)*dy, x + (i-1)*dx

            if not is_valid(ny, nx):
                return False, (ny, nx), c

            vis_pts[py][px] += 1
            if grid[ny][nx] == '#':
                return True, (py, px), c

            c+=1
            i+=1

    def solve_cycle():
        cdir = (-1, 0) # go up
        cpos = start_me
        vis: set[tuple[int, int, tuple[int, int]]] = set()
        while True:
            more, (ny, nx), _ = cont(*cpos, *cdir)
            if not more:
                return False
            cycle = (ny, nx, cdir) in vis
            if cycle:
                return True

            vis.add((ny, nx, cdir))
            cdir = turn_right(*cdir)
            cpos = (ny, nx)

    c = 0

    for ry, row in enumerate(grid):
        for cx, e in enumerate(row):
            if (ry, cx) != start_me and e == '.':
                grid[ry][cx] = '#'
                c += solve_cycle()
                grid[ry][cx] = '.'

    return c


class Testday06(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """....#.....
                        .........#
                        ..........
                        ..#.......
                        .......#..
                        ..........
                        .#..^.....
                        ........#.
                        #.........
                        ......#...
                    """
        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 41)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 6)


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



