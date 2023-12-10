from random import randint
from utils import lines as flines, bench


def sat(hold, t, d):
    return hold * (t - hold) > d

@bench
def get_pos(t, d):
    cnt = 0
    for hold in range(t+1):
        if sat(hold, t, d):
            cnt += 1

    return cnt


@bench
def init_pos_bin(t, d):
    # why so slow :V
    # [get_pos_bin(42899189,308117012911467)] Time taken: 1.407925067s
    # find the first 1
    pos = -1
    cnt = 0
    steps = t
    while steps > 0:
        for j in range(0, t+1, steps):
            cnt += 1
            if sat(j, t, d):
                print("[init_pos_bin] steps", steps)
                pos = j
                break

        if pos != -1:
            break

        steps //=2

    print("[init_pos_bin] iters", cnt)
    return pos


@bench
def init_pos_rand(t, d):
    cnt = 0
    pos = -1
    for i in range(t+1):
        pos = randint(0, t)
        cnt += 1
        if sat(pos, t, d):
            break

    print("init find (rand)", cnt)
    return pos


@bench
def get_pos_bin(t, d):
    pos = init_pos_bin(t, d)
    pos2 = init_pos_rand(t, d)
    assert sat(pos, t, d) == sat(pos2, t, d), f"bin pos = {pos}, rand pos = {pos2}"
    assert pos != -1, "At least one true should be present"

    first, last = None, None
    start, end = 0, pos
    cnt = 0
    # find the first pos of True
    while start <= end:
        mid = start + (end-start) // 2
        cnt += 1
        if sat(mid, t, d):
            first = mid
            end = mid - 1
        else:
            start = mid + 1


    print("first pos", cnt)

    start, end = pos, t+1
    cnt = 0
    # find the last pos of True
    while start <= end:
        mid = start + (end-start) // 2
        cnt += 1
        if sat(mid, t, d):
            last = mid
            start = mid + 1
        else:
            end = mid - 1

    assert last is not None and first is not None, f"{last=}, {first=}"
    print("first pos", cnt)

    return last - first + 1


def remove_spaces(line: str):
    return filter(lambda x: x.strip(), line.split(':')[1].split(' '))


def one():
    def parser(fpath: str):
        lines = flines(fpath)
        times = list(map(int, remove_spaces(lines[0])))
        dist = list(map(int, remove_spaces(lines[1])))
        return times, dist

    times, dist = parser("6.in1")
    ans = 1
    for time, dist in zip(times, dist):
        got = get_pos(time, dist)
        ans *= got

    print("ONE:", ans)


def two():
    def parser(fpath: str):
        lines = flines(fpath)
        times = int(''.join(remove_spaces(lines[0])))
        dist = int(''.join(remove_spaces(lines[1])))
        return int(times), int(dist)

    time, dist = parser("6.in1")
    # got = get_pos(time, dist)
    got = get_pos_bin(time, dist)
    # assert got == got
    ans = got
    print("TWO:", ans)


one()
two()
