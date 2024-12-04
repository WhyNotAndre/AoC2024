import re

fp = r""  # path to input file
with open(fp, 'r') as f:
    contents = f.read().split('\n')

damn = [line for line in contents]
length = len(damn[1])

def patternmatch(str):
    pattern = r'XMAS'
    patternrev = r'SAMX'    # reversed
    res1 = re.findall(pattern, str)
    res2 = re.findall(patternrev, str)
    return len(res1) + len(res2)

def checkV(arr, hPos):
    varr = [item[hPos] for item in arr]
    r1 = patternmatch(''.join(varr))
    return r1

def checkH(arr, vPos):
    harr = arr[vPos]
    r2 = patternmatch(harr)
    return(r2)


finresH = 0; finresV = 0
for i in range(len(damn)):
    finresH += checkH(damn, i)

for j in range(len(damn[0])):
    finresV += checkV(damn, j)


def print_diagonals(damn):
    r3 = 0; r4 = 0; r5 = 0; r6 = 0
    if not damn or not damn[0]:
        return

    n = len(damn)

    for start_col in range(n):
        row, col = 0, start_col
        diagonal = []
        while row < n and col >= 0:
            diagonal.append(damn[row][col])
            row += 1
            col -= 1
        r3 += patternmatch(''.join(diagonal))

    for start_row in range(1, n):
        row, col = start_row, n - 1
        diagonal = []
        while row < n and col >= 0:
            diagonal.append(damn[row][col])
            row += 1
            col -= 1
        r4 += patternmatch(''.join(diagonal))


    for start_col in range(n):
        row, col = 0, start_col
        diagonal = []
        while row < n and col < n:
            diagonal.append(damn[row][col])
            row += 1
            col += 1
        r5 += patternmatch(''.join(diagonal))

    for start_row in range(1, n):
        row, col = start_row, 0
        diagonal = []
        while row < n and col < n:
            diagonal.append(damn[row][col])
            row += 1
            col += 1
        r6 += patternmatch(''.join(diagonal))

    return r3 + r4 + r5 + r6

print(finresH + finresV + print_diagonals(damn))
