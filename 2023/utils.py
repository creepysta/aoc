def lines(fpath: str) -> list[str]:
    with open(fpath, 'r') as f:
        return [line.strip("\r\n ") for line in f]
