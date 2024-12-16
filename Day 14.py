import pandas as pd
import re

inp = r'' # path to input file

with open(inp) as f:
    spl = f.read().split("\n")
    
mm = [[int(m) for m in re.findall(r'(-?\d+)', sp)] for sp in spl]

df = pd.DataFrame(0, index=range(103), columns=range(101))

for m in mm:
    df.iat[m[1], m[0]]  = int(df.iat[m[1], m[0]]) + 1
    
xind=m[0]; yind=m[1]
for iter in range(100):
    for m in mm:
        xind = m[0]
        yind = m[1]
        # check index
        if yind+m[3] in range(df.shape[0]) and xind+m[2] in range(df.shape[1]):
            df.iat[yind+m[3], xind+m[2]] = int(df.iat[yind+m[3], xind+m[2]]) + 1
            df.iat[yind, xind] = int(df.iat[yind, xind]) - 1
            xind += m[2]; yind += m[3]
            m[0] = xind
            m[1] = yind
            continue
        else:
            df.iat[yind, xind] = int(df.iat[yind, xind]) - 1
            if yind + m[3] not in range(df.shape[0]):
                if yind + m[3] < 0:
                    yind = df.shape[0] - abs(yind + m[3])
                else:
                    yind = m[3] - abs(yind - df.shape[0])
            else:
                yind += m[3]
                    
            if xind + m[2] not in range(df.shape[1]):
                if xind + m[2] < 0:
                    xind = df.shape[1] - abs(xind + m[2])
                else:
                    xind = m[2] - abs(xind - df.shape[1])
            else:
                xind += m[2]
            
            df.iat[yind, xind] = int(df.iat[yind, xind]) + 1   
            m[0] = xind
            m[1] = yind


s1 = df.iloc[:df.shape[0]//2, :df.shape[1]//2].sum().sum()
s2 = df.iloc[df.shape[0]//2 + 1:, :df.shape[1]//2].sum().sum()
s3 = df.iloc[:df.shape[0]//2, df.shape[1]//2 + 1:].sum().sum()
s4 = df.iloc[df.shape[0]//2 + 1:, df.shape[1]//2 + 1:].sum().sum()

print(s1*s2*s3*s4)
