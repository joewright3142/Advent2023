from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput22.txt'
import math

with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')

for i in range(len(lines)):
    lines[i]=lines[i].split('~')
    
    lines[i][0]=lines[i][0].split(',')
    lines[i][1]=lines[i][1].split(',')
    for j in range(len(lines[i])):
        for k in range(len(lines[i][j])):
            lines[i][j][k]=int(lines[i][j][k])
lines.sort(key=lambda x:(x[0][2],x[1][2]))
    
tower=[[[0 for i in range(10)] for j in range(10)] for k in range(400)] #(x,y,z)
tower=np.array(tower)

dic={}
def bricksfall():
    for i in range(len(lines)):
        brick=lines[i]
        h=brick[0][2]
        ht=brick[1][2]-brick[0][2]+1
        xst,yst,xend,yend=brick[0][0],brick[0][1],brick[1][0],brick[1][1]
        while h>=1 and np.sum(tower[h-1,xst:xend+1,yst:yend+1])==0: #move down
            brick[0][2]-=1
            brick[1][2]-=1
            h-=1
        tower[h:h+ht,xst:xend+1,yst:yend+1]=(i+1)
        dic[i+1]=((h,h+ht),(xst,xend+1),(yst,yend+1))
bricksfall()
    
####How to do better...
#for a given brick, we can look above. the 
#75 sits above 17...
#look up 1, get brickid, look down.
#zxy 

def part1(i):
    bID=i+1
    h=dic[i+1][0][1]
    sqs=dic[i+1]
    bAbv=set()
    for j in range(sqs[1][0],sqs[1][1]): #xy
        for k in range(sqs[2][0],sqs[2][1]):
            if tower[h][j][k]!=0:
                bAbv.add(tower[h][j][k])
    u=h-1
    aboves=[0 for i in range(len(bAbv))]
    bAbv=list(bAbv)
    for j in range(len(bAbv)):
        sqs=dic[bAbv[j]]
        for k in range(sqs[1][0],sqs[1][1]): #xy
            for l in range(sqs[2][0],sqs[2][1]):
                if tower[u][k][l] not in {bID,0}: #unaffected
                    print(tower[u][k][l],k,l)
                    aboves[j]=1
    if sum(aboves)==len(aboves):
        return 1
    return 0
                    
#flag=1 can remove
#flag=0 can't remove
tot=0
#405  invariant => 895 variant
for i in range(len(lines)):
    tot+=part1(i)
print(tot)
#Part 2, disintegrating each brick., falling can only happen upwards
#Might be easiest to make a falls link dic...
#16174 too low
#if two falls

#sometimes a and b will fall, this will cause c to fall
#recursive call the algo...
#lazily adapt part1
def part2(i):
    sub=0
    bID=i+1
    q=deque([bID])
    isdstry={0,bID}
    while q:
        u=q.popleft()
        isdstry.add(u)
        h=dic[u][0][1]
        sqs=dic[u]
        bAbv=set()
        for j in range(sqs[1][0],sqs[1][1]): #xy
            for k in range(sqs[2][0],sqs[2][1]):
                if tower[h][j][k]!=0:
                    bAbv.add(tower[h][j][k])
        u=h-1
        aboves=[0 for i in range(len(bAbv))]
        bAbv=list(bAbv)
        for j in range(len(bAbv)):
            sqs=dic[bAbv[j]]
            for k in range(sqs[1][0],sqs[1][1]): #xy
                for l in range(sqs[2][0],sqs[2][1]):
                    if tower[u][k][l] not in isdstry: #unaffected
                        aboves[j]=1 #not falling
            if aboves[j]==0:
                q.append(bAbv[j])
                sub+=1
    return sub
                
tot=0
for i in range(len(lines)):
    tot+=part2(i)
print(tot)
    
    


