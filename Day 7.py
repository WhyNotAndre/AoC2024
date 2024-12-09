from itertools import product
from operator import add, mul
import re

inp = r'' # path to input file

with open(inp) as f:
    lines = f.read().strip()

lst = [list(map(int, re.findall("\\d+", line))) for line in lines.split("\n")]


operators = [add, mul]
dct = []

for l in lst:
    operator_combinations = product(operators, repeat=len(l) - 1)
    for ops in operator_combinations:
        result = l[0]
        rs = l[1]
        for i, op in enumerate(ops, start=1):
            try:
                rs = op(rs, l[i + 1])
            except:
                break
        if rs == result:
            dct.append(int(result))

print(sum(set(dct)))
