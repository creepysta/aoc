import sys
import unittest

from contextlib import redirect_stdout

def parse(content: str):
    line = [list(line.strip()) for line in content.split("\n") if len(line.strip()) ][0]
    return list(map(int, line))


EMPTY_BLOCK = -9999999
AVL_ID = -int(1e12)

def part1(content: str):
    nums = parse(content)
    idx = 0
    rv = []
    for parity, block in enumerate(nums):
        fill = idx
        if parity % 2 == 0:
            # storage
            fill = idx
            idx += 1
        else:
            # empty
            fill = EMPTY_BLOCK

        for _ in range(block):
            rv.append(fill)

    i, ri = 0, len(rv) - 1
    while i < ri:
        if rv[i] == EMPTY_BLOCK and rv[ri] != EMPTY_BLOCK:
            rv[i], rv[ri] = rv[ri], rv[i]
            ri -= 1
            i += 1

        if rv[i] != EMPTY_BLOCK:
            i += 1

        if rv[ri] == EMPTY_BLOCK:
            ri -= 1


    ans = sum([i*x for i, x in enumerate(rv) if x != EMPTY_BLOCK ])
    print(rv)

    return ans


def part2(content: str) -> int:
    nums = parse(content)
    idx = 0
    rv = []

    files: dict[int, tuple[int, int]] = {}
    em_blocks: list[tuple[int, int]] = []
    max_file_id = 0
    for parity, block in enumerate(nums):
        fill = idx
        if parity % 2 == 0:
            # storage
            fill = idx
            max_file_id = max(max_file_id, idx)
            files[fill] = (block, len(rv))
            idx += 1
        else:
            # empty
            fill = EMPTY_BLOCK
            if not block:
                continue

            em_blocks.append((block,len(rv)))

        for _ in range(block):
            rv.append(fill)

    while max_file_id >= 0:
        sz, frv_id = files[max_file_id]
        em_id, em_size = AVL_ID, AVL_ID
        for i, (em_sz, erv_id) in enumerate(em_blocks):
            if sz <= em_sz:
                em_blocks[i] = (em_sz - sz, erv_id + sz)
                em_id = erv_id
                em_size = em_sz
                break

        # print(max_file_id, frv_id, sz, em_id, em_size)

        condition = (
            em_id == AVL_ID
            # ask is to compact data, we should only look for empty blocks
            # at a lower index than files
            or frv_id < em_id
        )
        if condition:
            max_file_id -= 1
            continue

        # if frv_id < em_id:
        #     print(max_file_id, frv_id, sz, em_id, em_size)

        # got a block
        for i in range(sz):
            rv[em_id + i] = max_file_id

        # got a block
        for i in range(sz):
            rv[frv_id + i] = EMPTY_BLOCK


        max_file_id -= 1

    print(rv)

    ans = sum([i*x for i, x in enumerate(rv) if x != EMPTY_BLOCK])
    return ans


class Testday09(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """
        2333133121414131402
        """

        self.stdout = sys.stdout
        sys.stdout = sys.stderr
        return super().setUp()

    def tearDown(self) -> None:
        sys.stdout = self.stdout

    def test_part_1(self):
        got = part1(self.input)
        self.assertEqual(got, 1928)

    def test_part_2(self):
        got = part2(self.input)
        self.assertEqual(got, 2858)



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



