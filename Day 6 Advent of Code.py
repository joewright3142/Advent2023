import math
import numpy as np
import time
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput6.txt'
with open(filepath,'r') as f:
    lines=f.readlines()


for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split()[1:]
    
def times(lines):
    arr=[]
    for i in range(len(lines[0])):
        res,record,time=0,int(lines[1][i]),int(lines[0][i])
        for j in range(time):
            dist=(time-j)*j
            if dist>record:
                res+=1
        arr.append(res)
    return arr

arr=times(lines)
np.prod(arr)

l1=[["".join(lines[0])],["".join(lines[1])]]
#(time-j)*j>261119210191063

def qf(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/2*a
    x2=(-b-math.sqrt(b**2-4*a*c))/2*a
    return x1,x2,abs(int(x2)-int(x1))

s=time.time()
qf(-1,int(l1[0][0]),-int(l1[1][0]))
f=time.time()
print('QF',f-s)

s=time.time()
times(l1)
f=time.time()
print("BF",f-s)


