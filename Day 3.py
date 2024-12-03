import re
sum1 = 0; sum2 = 0; state = False

fpath = r"" # path to input file
with open(fpath, 'r') as f:
    contents = f"do(){f.read()}"  # enable mul instructions

def find_entries(text):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, text)
    return matches

# Part 1
res = find_entries(contents)

for r in res:
    sum1 += int(r[0]) * int(r[1])

# Part 2
do = r'\bdo\(\)'; dont = r'\bdon\'t\(\)'
sections = re.split(f'({do}|{dont})', contents)

for section in sections:
    section = section.strip()
    
    # if re.fullmatch(do, section):
    #     state = True
    # elif re.fullmatch(dont, section):
    #     state = False
    # elif state:
    #     res = find_entries(section)
    #     for r in res:
    #         sum2 += int(r[0]) * int(r[1])

    state = re.fullmatch(do, section) is not None or (re.fullmatch(dont, section) is None and state)
    if state:
        res = find_entries(section)
        for r in res:
            sum2 += int(r[0]) * int(r[1])

print(f"{sum1}\n{sum2}")
