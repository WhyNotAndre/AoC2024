import re

inp = r'' # path to input file

with open(inp) as f:
    spl = f.read().split("\n\n")
 
def find_matches(text):
    matches = re.findall(r'(\d+)', text)
    mm = [int(m) for m in matches]
    return mm
  
_ = 0  
for splt in spl:
    numx = [find_matches(splt)[0], find_matches(splt)[2]]
    targx = find_matches(splt)[4]
    numy = [find_matches(splt)[1], find_matches(splt)[3]]
    targy = find_matches(splt)[5]

    for i in range(100):
        for j in range(100):
            if numx[0]*i + numx[1]*j == targx:
                if numy[0]*i + numy[1]*j == targy:
                    _ += (i*3+j)
                    break

print(_)
