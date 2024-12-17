# =============================================================================
# FCK THIS SOKOBAN SHT
# =============================================================================

import pandas as pd
import numpy as np

inp = r'' # path to input file

with open(inp) as f:
    spl = f.read().split("\n\n")
    
s1 = [list(s) for s in spl[0].split("\n")]
df = pd.DataFrame(s1)
moves = spl[1]

# get initpos
arr = df.to_numpy()
res = np.where(arr == "@")
locy, locx = res[0][0], res[1][0]


def load(fp):
    with open(fp) as f:
        spl = f.read().split("\n\n")
        
    s1 = [list(s) for s in spl[0].split("\n")]
    df = pd.DataFrame(s1)
    arr = df.to_numpy()
    
    moves = spl[1].strip()
    return arr, moves


def isvalid(arr, pos):
    y, x = pos
    return 0 <= y < arr.shape[0] and 0 <= x < arr.shape[1] and arr[y, x] != '#'


def boxpush(arr, locy, locx, direction):
    boxy = locy + direction[0]
    boxx = locx + direction[1]
    
    if arr[boxy, boxx] != 'O':
        return False  # no box to push

    while True:
        nboxy = boxy + direction[0]
        nboxx = boxx + direction[1]
        
        if not isvalid(arr, (nboxy, nboxx)):
            return False  # cant push further
        
        if arr[nboxy, nboxx] == 'O':
            boxy, boxx = nboxy, nboxx 
        else:
            break

    while True:
        arr[boxy + direction[0], boxx + direction[1]] = 'O'
        arr[boxy, boxx] = ' '
        
        boxy -= direction[0]
        boxx -= direction[1]
        
        if arr[boxy, boxx] != 'O':
            break

    return True


def fmove(arr, moves):
    
    # get init @
    res = np.where(arr == "@")
    locy, locx = res[0][0], res[1][0]

    directions = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

    for move in moves:
        if move in directions:
            shift = directions[move]
            newlocy = locy + shift[0]
            newlocx = locx + shift[1]
            
            if isvalid(arr, (newlocy, newlocx)):

                if arr[newlocy, newlocx] == 'O':
                    if boxpush(arr, locy, locx, shift):
                        arr[locy, locx] = '.'
                        locy, locx = newlocy, newlocx
                        arr[locy, locx] = '@'
                else:
                    arr[locy, locx] = '.'
                    locy, locx = newlocy, newlocx
                    arr[locy, locx] = '@'
                    
    return arr


def main(fpath):
    sum = 0
    arr, moves = load(fpath)
    arr = fmove(arr, moves)

    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            if arr[y,x] == "O":
                sum += (100*y+x)
    return sum
        
print(main(inp))
