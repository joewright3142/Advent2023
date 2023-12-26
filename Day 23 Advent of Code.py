from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput23.txt'
import math

with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    
#No revisiting, standard isvis
dxns=((0,1),(1,0),(0,-1),(-1,0))
spec={'>','<','^','v'}
passdic={(0,1):'>',(1,0):'v',(0,-1):'<',(-1,0):'^'}
source,sink=(0,1),(140,139)


def dfsP1(p,d,path): #need to find max distance... (not min)
    if p==sink:
        #print("YEEEEEEEEEEEEEEE")
        return d
    res=0
    y,x=p
    for i in dxns:
        dy,dx=i
        if 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
            if lines[y+dy][x+dx]=='.' or  passdic[i]==lines[y+dy][x+dx]:
                if (y+dy,x+dx) not in path:
                    res=max(res,dfsP1((y+dy,x+dx),d+1,path.union({(y+dy,x+dx)})))
    return res

dfsP1(source,0,set())#need to find max
#########Part 2###########
# import sys
# sys.setrecursionlimit(4000)
# paths=set()
# def dfsP2(p,d,path): #need to find max distance... (not min)
#     if tuple(path) in paths:
#         return
#     paths.add(tuple(path))
#     if p==sink:
#         print(d)
#         return d
#     res=0
#     y,x=p
#     for i in dxns:
#         dy,dx=i
#         if 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
#             if lines[y+dy][x+dx]=='.' or  lines[y+dy][x+dx] in spec:
#                 if (y+dy,x+dx) not in path:
#                     res=max(res,dfsP2((y+dy,x+dx),d+1,path.union({(y+dy,x+dx)})))
#     return res

# dfsP2(source,0,set())#need to find max
#trick-corridors
jns=[source,sink]
find={'>','<','^','v','.'}
for y in range(len(lines)):
    for x in range(len(lines)):
        if lines[y][x] in find:
            ct=0
            for dy,dx in dxns:
                if 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
                    if lines[y+dy][x+dx] in find:
                        ct+=1
            if ct>2:
                jns.append((y,x))
            if ct==4:
                print(y,x)
#with corridors, we may only visit each node once...
#might have to append source sink
#next go a graph x=(y,d)
#need length
v=np.array([list(i) for i in lines])
g=defaultdict(list)
for i in range(len(jns)): #bfs until another jn
    for m in dxns:
        dy,dx=m
        y,x=jns[i][0],jns[i][1]
        if (0>x+dx or 0>y+dy or x+dx>=len(lines) or y+dy>=len(lines)) or lines[y+dy][x+dx] not in find :
            continue
        q=deque([(y+dy,x+dx,1)])
        isvis={(y,x)}
        while q:
            u=q.popleft()
            print(u)
            y,x=u[0],u[1]
            if (y,x) in isvis:
                continue
            if (y,x) in jns:
                print("yee")
                g[(jns[i][0],jns[i][1])].append(((y,x),u[2]))
                break
            isvis.add((y,x))
            for dy,dx in dxns:
                if 0<=x+dx<len(lines) and 0<=y+dy<len(lines):
                        if lines[y+dy][x+dx] in find and (y+dy,x+dx) not in isvis:
                            q.append((y+dy,x+dx,u[2]+1))
     
#we may now adapt the recursive algo
def dfsP2(p,d,path): #can't visit same node twice hence path
    if p==sink:
        print("yeee")
        print(d)
        return d
    res=0
    
    for j in g[p]:
        if j[0] not in path:
            res=max(res,dfsP2(j[0],d+j[1],path.union({j[0]})))
    return res

dfsP2(source,0,set())
                      
            
        
        
    

    

    
                 
        