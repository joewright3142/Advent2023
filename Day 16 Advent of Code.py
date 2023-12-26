from copy import deepcopy
import numpy as np
from collections import deque
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput16.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')
        lines[i]=list(lines[i])

dxns={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
source=(0,0,0) #RDLU 
def motion(v):
    y,x,d=v
    Next=[]
    dy,dx=dxns[d]
    if 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
        if lines[y+dy][x+dx]=='|' and d in {0,2}: #split v
            Next.append((y+dy,x+dx,1))
            Next.append((y+dy,x+dx,3))
        elif lines[y+dy][x+dx]=='-' and d in {1,3}: #split h
            Next.append((y+dy,x+dx,0))
            Next.append((y+dy,x+dx,2))
        elif lines[y+dy][x+dx]=='/':
            if d==0:
                Next.append((y+dy,x+dx,3))
            elif d==1:
                Next.append((y+dy,x+dx,2))
            elif d==2:
                Next.append((y+dy,x+dx,1))
            elif d==3:
                Next.append((y+dy,x+dx,0))
        elif lines[y+dy][x+dx]=='\\':
            if d==0:
                Next.append((y+dy,x+dx,1))
            elif d==1:
                Next.append((y+dy,x+dx,0))
            elif d==2:
                Next.append((y+dy,x+dx,3))
            elif d==3:
                Next.append((y+dy,x+dx,2))
        else:
            Next.append((y+dy,x+dx,d))
    return Next
            

source=(0,-1,0)  
def part1(source): #dfs possible stack overflow.
    isvis=set()
    n=motion(source)
    q=deque([])
    for i in n:
        q.append(i)
    while q :
        u=q.popleft()
        isvis.add(u)
        n=motion(u)
        for i in n:
            if i not in isvis:
                q.append(i)
        tot,s2=0,set()
        
    for i in isvis:
        if i[0:2] not in s2:
            s2.add(i[0:2])
    return len(s2)

part1((0,-1,0))
            
v=np.array(lines)
#def part2
sources=[]
def part2():
    bsf=0
    for i in range(len(lines)):
        sources.append((i,-1,0)) #first col
        sources.append((-1,i,1)) #first row
        sources.append((i,len(lines),2)) #last col    
        sources.append((len(lines),i,3)) #last row
    for i in sources:
        v=part1(i)
        bsf=max(bsf,v)
    return bsf

part2()