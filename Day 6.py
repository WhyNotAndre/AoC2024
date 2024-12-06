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
            print('trigger turn')
            if iter < 3:
                iter += 1 if iter < 3 else 0
            else:
                iter = 0
        
    except IndexError:  # CHECK OOB (NOT WORKING SOMEHOW)
        print(np.sum(arr=='+')+1) # COMPENSATE FOR LAST STEP BEFOR OOB
        a = False
