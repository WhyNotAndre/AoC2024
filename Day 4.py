# Disclaimer: 
# I ABSOLUTELY HATE THIS EXACT PUZZLE, DON'T BLAME ME FOR STUPID SOLUTION, 
# BLAME AUTHORS FOR STUPID PUZZLES INSTEAD
import re

fp = r""  # path to input file
with open(fp, 'r') as f:
    contents = f.read().split('\n')

damn = [line for line in contents]
length = len(damn[1])

# Part 1
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


def diagonals(damn):
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

print(finresH + finresV + diagonals(damn))

# Part 2
def patternmatch2(str):
    rs = re.findall(f"{r'MMASS'}|{r'MSAMS'}|{r'SSAMM'}|{r'SMASM'}", str)    # all combinations of 1,3,5,7,9th elem in 3x3
    # print(rs)
    return rs

def extract_3x3_blocks(matrix):
    blocks = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            block = [row[j:j+3] for row in matrix[i:i+3]]
            blocks.append(block)
    return blocks

blocks = extract_3x3_blocks(damn)

crosses = 0
for blk in blocks:
    _ = ''.join(blk)
    __ = _[0] + _[2] + _[4] + _[6] + _[8]   # get this stupid cross
    crosses += len(patternmatch2(__))
print(crosses)
