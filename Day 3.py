import re

fpath = r"" # path to input file

with open(fpath, 'r') as f:
    contents = f.read()

def find_entries(text):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, text)
    return matches

res = find_entries(contents)

# Part 1
sum = 0
for r in res:
    sum += int(r[0])*int(r[1])

print(sum)
