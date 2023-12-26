from copy import deepcopy
import heapq 
import numpy as np
from collections import deque
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput17.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')
        lines[i]=list(lines[i])
        for j in range(len(lines[i])):
            lines[i][j]=int(lines[i][j])
lines=np.array(lines)

dxns={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)} #RDLU
Next={0:(0,1,3),1:(0,1,2),2:(1,2,3),3:(0,2,3)}
lines=[
'2413432311323',
'3215453535623',
'3255245654254',
'3446585845452',
'4546657867536',
'1438598798454',
'4457876987766',
'3637877979653',
'4654967986887',
'4564679986453',
'1224686865563',
'2546548887735',
'4322674655533']
#lines=['1'*100 for i in range(100)]
for i in range(len(lines)):
    lines[i]=list(lines[i])
    for j in range(len(lines[i])):
        lines[i][j]=int(lines[i][j]) #make it say 14....
        # if i!=j and i+1!=j:
        #     lines[i][j]=100
lines=np.array(lines)
q=[]
def part1(lines):
    q=[]
    dist=[[[[10**6 for i in range(len(lines[0]))] for j in range(len(lines))] for k in range(4)] for l in range(4)]
    dist=np.array(dist)
    dist[0][0][0][0]=0 #RDLU
    dist[1][0][0][0]=0 #dxn,ct,y,x
    
    #DIJKSTRAS+ 
    q=[(0,0,0,0,0),(0,1,0,0,0)]
    
                
            
    #this should be doable with dijkstra's
    heapq.heapify(q)
    isvis=set() #sources visited....
    l=[]
    while q:
        u=heapq.heappop(q)
        d,dxn,ct,y,x=u
        if (dxn,ct,y,x) in isvis:
            continue
        isvis.add((dxn,ct,y,x))
        if (y,x)==(len(lines)-1,len(lines[0])-1):
            l.append(d)
        mvs=Next[dxn] #next moves
        for v in mvs:
            dy,dx=dxns[v]
            if ct==2 and v==dxn:
                continue
            if 0<=x+dx<len(lines[0]) and 0<=y+dy<len(lines):
                dxnct=0
                if v==dxn: 
                    dxnct=ct+1
                if d+lines[y+dy][x+dx]<=dist[v][dxnct][y+dy][x+dx]:
                    dist[v][dxnct][y+dy][x+dx]=d+lines[y+dy][x+dx]
                    heapq.heappush(q,(d+lines[y+dy][x+dx],v,dxnct,y+dy,x+dx))
    return min(l)
part1(lines)
#1221 too low
#1248 too high
#1234 too low
#NOT 1244 
#Not 1239
###Part2
def part2(lines):
    dist=[[[[10**6 for i in range(len(lines[0]))] for j in range(len(lines))] for k in range(11)] for l in range(4)]
    dist=np.array(dist)
    dist[0][0][0][0]=0 #RDLU
    dist[1][0][0][0]=0 #dxn,ct,y,x
    
    #DIJKSTRAS+ 
    q=[(0,0,0,0,0),(0,1,0,0,0)]
    #this should be doable with dijkstra's
    heapq.heapify(q)
    isvis=set() #sources visited....
    l=[]
    while q:
        u=heapq.heappop(q)
        d,dxn,ct,y,x=u
        if (dxn,ct,y,x) in isvis:
            continue
        isvis.add((dxn,ct,y,x))
        if (y,x)==(len(lines)-1,len(lines[0])-1):
            l.append(d)
        mvs=Next[dxn] #next moves
        for v in mvs:
            dy,dx=dxns[v]
            if ct<3 and v!=dxn:
                continue
            elif ct==9 and v==dxn:
                continue
            if 0<=x+dx<len(lines[0]) and 0<=y+dy<len(lines):
                dxnct=0
                if v==dxn: 
                    dxnct=ct+1
                if d+lines[y+dy][x+dx]<=dist[v][dxnct][y+dy][x+dx]:
                    dist[v][dxnct][y+dy][x+dx]=d+lines[y+dy][x+dx]
                    heapq.heappush(q,(d+lines[y+dy][x+dx],v,dxnct,y+dy,x+dx))
    return min(l)
part2(lines)


