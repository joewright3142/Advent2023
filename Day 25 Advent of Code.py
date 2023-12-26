from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput25.txt'
import math
import graphviz


with open(filepath,'r') as f:
    lines=f.readlines()
    
for i in range(len(lines)):
    lines[i]=lines[i].split(':')
    for j in range(1,len(lines[i])):
        
        lines[i][j]=lines[i][j].split()
        
dic=defaultdict(list)
for i in range(len(lines)):
    y=lines[i][0]
    for x in lines[i][1]:
        dic[y].append(x)
        dic[x].append(y)
#how to cut wires:
# import graphviz
# dot = graphviz.Graph(engine='neato')
# for i in dic:
#     dot.node(i)
#     for j in dic[i]:
#         dot.edge(i,j)

# dot.render('graph', view=True)
#For i in range:
print(dic['jzj'].pop(),
dic['vkb'].pop(),  #jzj
dic['vrx'].pop(),
dic['hhx'].pop(1) ,#vrx,
dic['nvh'].pop(2),
dic['grh'].pop(2))# nvh)

########
#l source vkb
l='vkb'
#r source
r='vrx'
#bfs
ans=[]
for i in (l,r):
    
    q=deque([i])
    isvis=set()
    while q:
        u=q.popleft()
        print(u)
        if u in isvis:
            continue
        isvis.add(u)
        
        for j in dic[u]:
            print(dic[u])
            q.append(j)
    ans.append(len(isvis))
            
    #bfs to draw both graphs
    #747
    
    ans
print(732*747)