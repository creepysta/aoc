import sys
import unittest

from contextlib import redirect_stdout
from itertools import product

def parse(content: str):
    lines = [line.strip() for line in content.split("\n") if len(line.strip()) ]
    rv: list[tuple[int, list[int]]] = []
    for line in lines:
        ls, rs = line.split(":")
        ints = map(int, rs.strip().split(" "))
        target = int(ls.strip())
        rv.append((target, list(ints)))

    return rv



def part1(content: str):
    lines = parse(content)

    def solve(comb, target: int, nums: list[int]) -> bool:
        rev = list(reversed(nums))
        cm = list(comb)
        while len(rev) > 1:
            a, b = rev.pop(), rev.pop()
            op = cm.pop()
            got = eval(op.join([str(a), str(b)]))
            rev.append(got)

        got = rev[0]
        return got == target

    def check(target: int, nums: list[int]) -> bool:
        ops = ['*', '+']
        places = len(nums) - 1
        for comb in product(ops, repeat=places):
           can = solve(comb, target, nums)
           if can:
               return True


        return False



    rv = sum(map(lambda x: x[0], filter(lambda x: check(x[0], x[1]), lines)))

    return rv


def part2(content: str) -> int:
    lines = parse(content)

    def solve(comb, target: int, nums: list[int]) -> bool:
        rev = list(reversed(nums))
        cm = list(comb)
        while len(rev) > 1:
            a, b = rev.pop(), rev.pop()
            op = cm.pop()
            if op == 'or':
                got = ''.join([str(a), str(b)])
                rev.append(int(got))
            else:
                got = eval(op.join([str(a), str(b)]))
                rev.append(got)

        got = rev[0]
        return got == target

    def check(target: int, nums: list[int]) -> bool:
        places = len(nums) - 1

        ops = ['*', '+']
        for comb in product(ops, repeat=places):
           can = solve(comb, target, nums)
           if can:
               return True

        ops = ['+', 'or']
        for comb in product(ops, repeat=places):
           can = solve(comb, target, nums)
           if can:
               return True

        ops = ['*', 'or']
        for comb in product(ops, repeat=places):
           can = solve(comb, target, nums)
           if can:
               return True

        ops = ['+', '*', 'or']
        for comb in product(ops, repeat=places):
           can = solve(comb, target, nums)
           if can:
               return True


        return False


    rv = sum(
        map(
            lambda x: x[0],
            filter(
                lambda x: check(x[0], x[1]),
                lines
            )
        )
    )

    return rv


class Testday07(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
            190: 10 19
            3267: 81 40 27
            83: 17 5
            156: 15 6
            7290: 6 8 6 15
            161011: 16 10 13
            192: 17 8 14
            21037: 9 7 18 13
            292: 11 6 16 20
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 3749)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 11387)



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



