# AT FIRST I THOUGHT I NEED CAFFEINE FOR THAT,
# NOW I THINK I NEED SEDATIVES

inp = r'' # path to input file

with open(inp, 'r') as f:
    paresdinp = f.read()
  
# lst = [line for line in paresdinp.split('\n\n')]
lst = [section.strip() for section in paresdinp.split('\n\n')]

# pgorder = [{int(line.split('|')[0]):int(line.split('|')[1])} for line in lst[0].splitlines()]
pgorder = {}
for line in lst[0].splitlines():
    x, y = map(int, line.split('|'))
    if x not in pgorder:
        pgorder[x] = []
    pgorder[x].append(y)

pgupdate = [line for line in lst[1].splitlines()]
parsedpgupdate = [[int(item) for item in upd.split(',')] for upd in pgupdate]

def isordered(update, pgorder):
    indexmap = {page: i for i, page in enumerate(update)}
    for x in pgorder:
        for y in pgorder[x]:
            if x in indexmap and y in indexmap:
                if indexmap[x] > indexmap[y]:  # x must come before y
                    return False
    return True

def findmidpage(update):
    midindex = len(update) // 2
    return update[midindex]

midpagesum = 0
# loop through each update, calc midpagesum

for update in parsedpgupdate:
    if isordered(update, pgorder):
        midpage = findmidpage(update)
        midpagesum += midpage

print(midpagesum)
