fpath = r""  # path to input file

with open(fpath, 'r') as f:
    contents = f.read()

lists_to_test = [[int(num) for num in line.split()] for line in contents.splitlines()]

def check_seq(lst):
    res1 = ""; res2 = ""
    for i in range(len(lst)-1):
        res1 = (lst[i + 1] > lst[i] and abs(lst[i + 1] - lst[i]) < 4) and (res1 or res1 == "")
    for i in range(len(lst)-1):
        res2 = (lst[i + 1] < lst[i] and abs(lst[i + 1] - lst[i]) < 4) and (res2 or res2 == "")
    return (res1, res2)
            
# PART 1
r=0
for l in lists_to_test:
    a, b = check_seq(l)
    if a or b:
        r += 1
print(r)

# PART 2
r = 0
for l in lists_to_test:
    for i in range(len(l)):
        lst = l[:i]+l[i+1:]
        a, b = check_seq(lst)
        if a or b:
            r += 1
            break
print(r)
