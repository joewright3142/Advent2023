from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
import math
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput21.txt'

with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=list(lines[i])
lines=np.array(lines)
def findst():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=='S':
                return (i,j)
s=findst()

lines[s[0]][s[1]]='.'
dxns=((0,1),(1,0),(0,-1),(-1,0))
#need to take 64 steps.
#bfs?
def part1():
    q=deque([(s,0)])
    isvis=set()
    makeable=set()
    dist=0
    while q:
        u=q.popleft()
        y,x=u[0]
        if (y,x) in isvis:
            continue
        isvis.add((y,x))
        if u[1]%2==0:
            makeable.add((y,x))
            
            
        for dy,dx in dxns:
            if lines[y+dy][x+dx]!='#':
                if u[1]<64 and 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
                    q.append(((y+dy,x+dx),u[1]+1))
    return len(makeable)
#7370, too high, we can only achieve the tiles with even distance
#part 2
#Strat use part 1 to find min dist to all points
####Create a new grid...
#how tho?
#get the 4 corners 
#65,65 weirdly, it should

q=deque([(s,0)])
isvis=set()
makeable=[]
dist=0
while q:
    u=q.popleft()
    y,x=u[0]
    if (y,x) in isvis:
        continue
    isvis.add((y,x))
    if u[1]%2==1:
        makeable.append((y,x,u[1]))
        
        
    for dy,dx in dxns:
        if  0<=x+dx<len(lines) and 0<=y+dy<len(lines) and lines[y+dy][x+dx]!='#':
            q.append(((y+dy,x+dx),u[1]+1))
#7370, too high, we can only achieve the tiles with even distance
#part 2
#for each of these, they can be made in the adjacent  grids-131 away...
steps=132
tot=0
maxproject=26501365//len(lines)
odd=(maxproject+1)**2
even=maxproject**2
odddiamonds=maxproject+1
evendiamonds=maxproject



#even grid
def grid(s,oddev):
    q=deque([(s,0)])
    isvis=set()
    makeable=[]
    dist=0
    while q:
        u=q.popleft()
        y,x=u[0]
        if (y,x) in isvis:
            continue
        isvis.add((y,x))
        if u[1]%2==oddev:
            makeable.append((y,x,u[1]))
        for dy,dx in dxns:
            if  0<=x+dx<len(lines) and 0<=y+dy<len(lines) and lines[y+dy][x+dx]!='#':
                q.append(((y+dy,x+dx),u[1]+1))
    return makeable
egrid=grid((65,65),0)
ogrid=grid((65,65),1)

ediamond,odiamond=[],[]
for i in egrid:
    if abs(i[0]-65)+abs(i[1]-65)>65:
        ediamond.append(i)
        
for i in ogrid:
    if abs(i[0]-65)+abs(i[1]-65)>65:
        odiamond.append(i)

def part2(n):
    tot=0
    t=len(ogrid)*(n+1)**2+len(egrid)*(n)**2-(n+1)*len(odiamond)+n*len(ediamond)
    return t

part2(26501365//len(lines))