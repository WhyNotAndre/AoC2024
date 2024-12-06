import numpy as np

inp = r'' # path to input file

with open(inp, 'r') as f:
    lines = f.readlines()

chars = [list(line.strip()) for line in lines]
arr = np.array(chars)

ind = np.where(arr=='^')
loc = (int(ind[0]), int(ind[1]))
locx = loc[1]
locy = loc[0]

iter = 0
direcs = ['U', 'R', 'D', 'L']

locx_hist = []
locy_hist = []


a = True
while a:
    try:
        currentdirec = direcs[iter]
        
        # SELECT DIRECTION
        if currentdirec == 'U': shiftx = 0; shifty = -1
        if currentdirec == 'R': shiftx = 1; shifty = 0
        if currentdirec == 'D': shiftx = 0; shifty = 1
        if currentdirec == 'L': shiftx = -1; shifty = 0
        # print(locx); print(locy)
        if arr[locy+shifty, locx+shiftx] != "#":
            arr[locy, locx] = "+"    # MARK PREV STEP AS VISITED
            locx += shiftx
            locy += shifty
            locx_hist.append(locx)
            locy_hist.append(locy)
            arr[locy, locx] = "^"    # RESET POS
            if locy < 0:    # ANOTHER OOB CHECK (WORKING)
                a = False
                print(np.sum(arr=='+'))
        else:
            # print('trigger turn')
            if iter < 3:
                iter += 1 if iter < 3 else 0
            else:
                iter = 0
        
    except IndexError:  # CHECK OOB (NOT WORKING SOMEHOW)
        print(np.sum(arr=='+')+1) # COMPENSATE FOR LAST STEP BEFOR OOB
        a = False
        

# part 2
with open(inp, 'r') as f:
    lines = f.readlines()

chars = [list(line.strip()) for line in lines]
arr = np.array(chars)
res = 0
ind = np.where(arr=='^')
loc = (int(ind[0]), int(ind[1]))
# idk y my arr has elem len of 1, so this garbage is to bypass this
lst = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def aaaa():       
    global res, lst
    res = False
    locx = loc[1]
    locy = loc[0]
    loopcnt = 0
    iter = 0
    direcs = ['U', 'R', 'D', 'L']

    a = True
    while a:
        if int(loopcnt) <= 33:  # assuming that if loc was visited less than 34 times, theres no infinite loop (seems  like it really is)
            try:
                currentdirec = direcs[iter]
                
                # SELECT DIRECTION
                if currentdirec == 'U': shiftx = 0; shifty = -1
                if currentdirec == 'R': shiftx = 1; shifty = 0
                if currentdirec == 'D': shiftx = 0; shifty = 1
                if currentdirec == 'L': shiftx = -1; shifty = 0
    
                # if arr[locy+shifty, locx+shiftx] != "#":
                #     try:
                #         _ = int(arr[locy, locx])
                #         if int(arr[locy, locx]) in [1,2,3,4,5,6,7,8,9]:
                #             arr[locy, locx] = int(arr[locy, locx]) + 1
                #         else:
                #             arr[locy, locx] = 1
                #     except:
                #         arr[locy, locx] = 1
                        
                        
                if arr[locy+shifty, locx+shiftx] != "#":
                    if arr[locy, locx] in lst:
                        arr[locy, locx] = lst[lst.index(arr[locy, locx]) + 1]
                    else:
                        arr[locy, locx] = lst[1]

    
                    loopcnt = lst.index(arr[locy, locx]) + 1
                    # print(loopcnt)
                    locx += shiftx
                    locy += shifty
                    # arr[locy, locx] = '^'
                    if locy < 0 or locx < 0 or locy > len(arr) - 1 or locx > len(arr) - 1: # exclude OOB
                        # a = False
                        break
                else:
                    if iter < 3:
                        iter += 1 if iter < 3 else 0
                    else:
                        iter = 0
                
            except:
                # a = False
                break
        else:    
            res = True
            break
        
    return res
        
        
total = 0
ar = []
for i in range(len(arr)):
    for j in range(len(arr)):
        
        with open(inp, 'r') as f:
            lines = f.readlines()
            
        # reset arr
        chars = [list(line.strip()) for line in lines]
        arr = np.array(chars)
        res = False
        ind = np.where(arr=='^')
        loc = (int(ind[0]), int(ind[1]))
        
        if arr[i,j] not in ['#', '^']:
            prev = arr[i,j]
            arr[i,j] = '#'  # change each . to # and check
            if aaaa(): total += 1    #; ar.append([i,j])
            # print(arr)
            # arr[i,j] = prev # this is probably useless
            
print(total)
        
