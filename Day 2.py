fpath = r""

with open(fpath, 'r') as f:
    contents = f.read()

lists_to_test = [[int(num) for num in line.split()] for line in contents.splitlines()]

def check_seq(lst):
    res1 = ""; res2 = ""
    for i in range(0, len(lst)-1):
        res1 = True if (lst[i+1] > lst[i] and abs(lst[i+1] - lst[i]) < 4 and (res1 == True or res1 == "") and lst[i+1] != lst[i]) else False
    for i in range(0, len(lst)-1):
        res2 = True if (lst[i+1] < lst[i] and abs(lst[i+1] - lst[i]) < 4 and (res2 == True or res2 == "") and lst[i+1] != lst[i]) else False
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
    for i in range(0, len(l)):
        lst = l[:i]+l[i+1:]
        a, b = check_seq(lst)
        if a or b:
            r += 1
            break
print(r)
