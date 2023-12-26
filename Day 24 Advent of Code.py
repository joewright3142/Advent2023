from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput24.txt'
import math


with open(filepath,'r') as f:
    lines=f.readlines()
    
# lines=[
# '19, 13, 30 @ -2,  1, -2',
# '18, 19, 22 @ -1, -1, -2',
# '20, 25, 34 @ -2, -2, -4',
# '12, 31, 28 @ -1, -2, -1',
# '20, 19, 15 @  1, -5, -3']
    
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split('@')
    for j in range(len(lines[i])):
        lines[i][j]=lines[i][j].split(',')
        for k in range(len(lines[i][j])):
            lines[i][j][k]=int(lines[i][j][k])

def willIntersect(i,j):
    x1,y1=lines[i][0][0],lines[i][0][1]
    x2,y2=lines[j][0][0],lines[j][0][1]
    m1=lines[i][1][1]/lines[i][1][0]
    m2=lines[j][1][1]/lines[j][1][0]
   
    if round(m1,5)==round(m2,5): #paralel
        return "no"
    c1=(y1-m1*x1)
    c2=(y2-m2*x2)
    xint=(c2-c1)/(m1-m2)
    yint=m1*xint+c1
    if x1<xint and lines[i][1][0]<0:
        return 'no'
    if x1>xint and lines[i][1][0]>0:
        return 'no'
    if x2<xint and lines[j][1][0]<0:
        return 'no'
    if x2>xint and lines[j][1][0]>0:
        return 'no'
    return (xint,yint)

#willIntersect(0,1)
collide=[]
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        v=willIntersect(i,j)
        if v!='no' and (2*10**14<=v[0]<=4*10**14 and 2*10**14<=v[1]<=4*10**14):
            collide.append((i,j))
        print(v)
        
print(len(collide))
#19786 too high...
##Def part 2

#6 lines, collision #likely to work, can test
#FSOLVE
from scipy.optimize import fsolve
from math import exp
#Part 2


#willIntersect(0,1)
collide=[]
return 


pos,vel=[],[]
for i in range(len(lines)):
    pos.append(lines[i][0])
    vel.append(lines[i][1])

xset,yset,zset=set(),set(),set()
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        if vel[i][0]==vel[j][0]: #xspeed
            cands=set()
            dist=pos[i][0]-pos[j][0] #
            for v in range(-1000,1000):
                
                if v!=vel[i][0] and dist%(vel[i][0]-v)==0:
                    cands.add(v)
            if len(xset)==0:
                xset=cands
            else:
                xset=xset&cands
        if vel[i][1]==vel[j][1]: #yspeed
            cands=set()
            dist=pos[i][1]-pos[j][1] #
            for v in range(-1000,1000):
                if v!=vel[i][1] and dist%(vel[i][1]-v)==0:
                    cands.add(v)
            if len(yset)==0:
                yset=cands
            else:
                yset=yset&cands
        if vel[i][2]==vel[j][2]: #yspeed
            cands=set()
            dist=pos[i][2]-pos[j][2] #
            for v in range(-1000,1000):
                if v!=vel[i][2] and dist%(vel[i][2]-v)==0:
                    cands.add(v)
            if len(zset)==0:
                zset=cands
            else:
                zset=zset&cands
xv,yv,zv=xset.pop(),yset.pop(),zset.pop()
l1=lines[0]
l2=lines[1]
def willIntersect2(l1,l2):
    x1,y1=l1[0][0],l1[0][1]
    x2,y2=l2[0][0],l2[0][1]
    
    m1=(l1[1][1]-yv)/(l1[1][0]-xv)
    m2=(l2[1][1]-yv)/(l2[1][0]-xv)
    c1=(y1-m1*x1)
    c2=(y2-m2*x2)
    xint=(c2-c1)/(m1-m2)
    yint=m1*xint+c1
    #we now have x and y
    #can we get t?
    t=(int(xint)-x1)/(l1[1][0]-xv)
    zint=l1[0][2]+(l1[1][2]-zv)*t
    return (xint,yint,zint)
int(sum(willIntersect2(l1,l2)))



lz=(lines[0],lines[1])
for i in range(len(lz)):
    for j in range(i+1,len(lz)):
        i=0
        j=1
        xp1,yp1,zp1=lz[i][0] #a
        xp2,yp2,zp2=lz[j][0] #c
        x1v=lz[i][1][0]-xv #b
        y1v=lz[i][1][1]-yv
        z1v=lz[i][1][2]-zv        
        x2v=lz[j][1][0]-xv #d
        y2v=lz[j][1][1]-yv
        z2v=lz[j][1][2]-zv
        x=(xp1*x2v-x1v*xp2)/(x2v-x1v)
        y=(yp1*y2v-y1v*yp2)/(y2v-y1v)
        z=(zp1*z2v-z1v*zp2)/(z2v-z1v)
        print(sum([x,y,z]))

APX, APY, APZ, AVX, AVY, AVZ = lines[0][0]+lines[0][1]
BPX, BPY, BPZ, BVX, BVY, BVZ = lines[1][0]+lines[1][1]
MA = (AVY-yv)/(AVX-xv)
MB = (BVY-yv)/(BVX-xv)
CA = APY - (MA*APX)
CB = BPY - (MB*BPX)
XPos = int((CB-CA)/(MA-MB))
YPos = int(MA*XPos + CA)
Time = (XPos - APX)//(AVX-xv)
ZPos = APZ + (AVZ - zv)*Time        

sum([XPos,YPos,ZPos])
559822754465977
578177720733043


#velocities found, now need to find the point.

                


    