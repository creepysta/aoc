with open("in1.in", "r") as f:
    inp = f.read()

def isUnique(string):
    ls = list(string); ls.sort()
    lss = list(set(string)); lss.sort()
    return ls == lss

def findUniqueSubstring(string, offset = 4):
    for i in range(len(string)):
        if isUnique(inp[i:i + offset]):
            print(inp[i:i + offset])
            return i + offset

print(f"Answer 1: {findUniqueSubstring(inp)}\nAnswer 2: {findUniqueSubstring(inp, offset = 14)}")
