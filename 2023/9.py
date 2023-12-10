from utils import lines as flines


def parser(fpath: str):
    lines = flines(fpath)
    nums = [[int(x) for x in line.split(' ')] for line in lines]
    return nums


def get_req_num(stack: list[list[int]], last: bool) -> int:
    rstack = stack[::-1]
    for i in range(1, len(rstack)):
        if last:
            pcurr = rstack[i-1]
            curr = rstack[i]
            last_el = curr[-1]
            p_last = pcurr[-1]
            curr.append(last_el + p_last)
        else:
            pcurr = rstack[i-1]
            curr = rstack[i]
            first_el = curr[0]
            p_first = pcurr[0]
            curr.insert(0, first_el - p_first)

    return rstack[-1][-1 if last else 0]


def calc_cd(nums: list[int], last: bool) -> int:
    stack = []
    stack.append(nums)
    while True:
        row = []
        prev = stack[-1]
        for i in range(len(prev)-1):
            row.append(prev[i+1]-prev[i])

        if not any(row):
            return get_req_num(stack, last)

        assert len(row) > 1
        stack.append(row)


def process(nums: list, last=True) -> int:
    assert len(nums) > 1
    d = nums[1] - nums[0]
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] != d:
            return calc_cd(nums, last)

    return nums[-1] + d if last else nums[0] - d


def one():
    nums = parser("9.in1")
    ans = 0
    for row in nums:
        got = process(row)
        ans += got

    print("ONE:", ans)

def two():
    nums = parser("9.in1")
    ans = 0
    for row in nums:
        got = process(row, False)
        # print("got:", got)
        ans += got

    print("TWO:", ans)


one()
two()
