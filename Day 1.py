fpath = r"" # path to input file

with open(fpath, 'r') as f:
    contents = f.read()

list = [line.split() for line in contents.splitlines()]

l1 = []; l2 = []; sum1 = 0; sum2 = 0

for l in list:
    l1.append(int(l[0]))
    l2.append(int(l[1]))
  
# PART 2
for item in l1:
    cnt = l2.count(item)
    sum2 += item*cnt
    
# PART 1
for i in range(len(l1)):
    sum1 += abs(min(l1) - min(l2))
    l1.pop(l1.index(min(l1)))
    l2.pop(l2.index(min(l2)))

print(f"{sum1}\n{sum2}")
