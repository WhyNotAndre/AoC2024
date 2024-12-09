inp = r'' # path to input file

with open(inp) as f:
    line = f.read()

lst = []

for i, elem in enumerate(line):
    if i % 2 == 0:
        for j in range(int(elem)):
            lst.append(int(i/2))
    else:
        for k in range(int(elem)):
            lst.append("")


stopflg = False
for i, item in enumerate(reversed(lst)):
    if item != "":
        for j, jtem in enumerate(lst):
            if jtem == "":
                if j < len(lst)-i-1:
                    lst[j] = item
                    lst[len(lst)-i-1] = ""
                    break
                else:
                    stopflg = True
    if stopflg:
        break

sum = 0
for n, num in enumerate(lst):
    if num != "":
        sum += n*num
print(sum)
