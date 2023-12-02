from utils import lines as flines


def parser(fpath: str):
    lines = flines(fpath)
    return lines


def one():
    parsed = parser("2.in1")
    ans = 0
    print("ONE:", ans)

def two():
    parsed = parser("2.in1")
    ans = 0
    print("TWO:", ans)


one()
two()
