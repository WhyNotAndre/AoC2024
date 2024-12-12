inp = r'' # path to input file

with open(inp) as f:
    line = f.read().split(" ")
    
def chk(length):
    stones = [int(stone) for stone in line]
    temp = []
    
    for iter in range(length):
        for stone in stones:
            if not stone:
                temp.append(1)
            elif not len(str(stone)) % 2:
                strstone = str(stone)
                split1 = int(strstone[:int(len(strstone)/2)])
                split2 = int(strstone[int(len(strstone)/2):])
                temp.append(split1)
                temp.append(split2)
            else:
                temp.append(stone*2024)
            stones = temp
            
        temp = []
    return len(stones)

print(chk(25))
