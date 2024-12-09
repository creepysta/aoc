import sys
import unittest

from pprint import pprint
from copy import deepcopy
from itertools import combinations
from collections import defaultdict
from contextlib import redirect_stdout
from typing import Any

def parse(content: str):
    return [line.strip() for line in content.split("\n") if len(line.strip()) ]


def place_chr(grid: list[Any], np: tuple[int, int]):
    grid[np[0]] = list(grid[np[0]])
    grid[np[0]][np[1]] = '#'
    grid[np[0]] = ''.join(grid[np[0]])


def part1(content: str):
    grid = parse(content)
    cgrid = deepcopy(parse(content))
    coll: dict[str, list[tuple[int, int]]]  = defaultdict(list)
    for y, row in enumerate(grid):
        for x, el in enumerate(row):
            if el == '.':
                continue

            coll[el].append((y, x))

    def is_valid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])


    placed: set[tuple[int, int]] = set()
    for _, arr in coll.items():
        for comb in combinations(arr, 2):
            p, q = comb
            dy, dx = q[0] - p[0], q[1] - p[1]
            p1 = p[0] - dy, p[1] - dx
            p2 = q[0] + dy, q[1] + dx

            if is_valid(*p1):
                placed.add(p1)
                place_chr(cgrid, p1)
            if is_valid(*p2):
                placed.add(p2)
                place_chr(cgrid, p2)


    pprint(cgrid)
    return len(placed)


def part2(content: str) -> int:

    grid = parse(content)
    cgrid = deepcopy(grid)

    coll: dict[str, list[tuple[int, int]]]  = defaultdict(list)
    for y, row in enumerate(grid):
        for x, el in enumerate(row):
            if el == '.':
                continue

            coll[el].append((y, x))

    def is_valid(y, x):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    placed: set[tuple[int, int]] = set()
    def place(key: str, start: tuple[int, int], dirc: tuple[int, int]):
        for i in range(1000):
            np = start[0] + i*dirc[0], start[1] + i*dirc[1]
            # print(np)
            if not is_valid(*np):
                break

            # el = grid[np[0]][np[1]]
            # not needed ??? wth
            # if el == key:
            #     continue

            place_chr(cgrid, np)
            placed.add(np)


    for key, arr in coll.items():
        for comb in combinations(arr, 2):
            p, q = comb
            dy, dx = q[0] - p[0], q[1] - p[1]
            place(key, p, (-dy, -dx))
            place(key, q, (dy, dx))


    pprint(cgrid)
    return len(placed)


class Testday08(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
            ............
            ........0...
            .....0......
            .......0....
            ....0.......
            ......A.....
            ............
            ............
            ........A...
            .........A..
            ............
            ............
        """
        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        final = """
            ......#....#
            ...#....0...
            ....#0....#.
            ..#....0....
            ....0....#..
            .#....A.....
            ...#........
            #......#....
            ........A...
            .........A..
            ..........#.
            ..........#.
        """
        got = part1(self.input)
        self.assertEqual(got, 14)

    def test_part_2(self):
        final = """
            ##....#....#
            .#.#....0...
            ..#.#0....#.
            ..##...0....
            ....0....#..
            .#...#A....#
            ...#..#.....
            #....#.#....
            ..#.....A...
            ....#....A..
            .#........#.
            ...#......##
        """
        got = part2(self.input)
        self.assertEqual(got, 34)



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



