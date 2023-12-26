from copy import deepcopy
import heapq 
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput18.txt'

with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')
        lines[i]=lines[i].split()
        lines[i]=list(lines[i])

grid=[[0 for i in range(1000)]  for i in range(1000)]
pos=(500,500)
grid[500][500]=1
#draw then use floodfill algo
dxn={'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}
for i in range(len(lines)):
    dy,dx=dxn[lines[i][0]]
    dist=int(lines[i][1])
    y,x=pos
    for j in range(1,dist+1):
        grid[y+j*dy][x+j*dx]=1
    pos=(y+dy*dist,x+dx*dist)


def insidePoint(grid):
    for i in range(len(grid)):
        if sum(grid[i])!=0:
            for j in range(len(grid[i])):
                if grid[i][j-1]==0 and grid[i][j]==1 and grid[i][j+1]==0:
                    st=(i,j+1)
                    return st
                    break
insidePoint(grid)
def part1(grid):
    st=insidePoint(grid)
    print(st)
    #bfs it
    q=deque([st])
    while q:
        u=q.popleft()
        y,x=u
        for i in dxn:
            dy,dx=dxn[i]
            if grid[y+dy][x+dx]==0:
                q.append((y+dy,x+dx))
                grid[y+dy][x+dx]=1
    tot=0
    for i in range(len(grid)):
        tot+=sum(grid[i])
    return tot

part1(grid)
#Part 2 
#Convert the hexadecimals
# lines=[
# 'R 6 (#70c710)',
# 'D 5 (#0dc571)',
# 'L 2 (#5713f0)',
# 'D 2 (#d2c081)',
# 'R 2 (#59c680)',
# 'D 2 (#411b91)',
# 'L 5 (#8ceee2)',
# 'U 2 (#caa173)',
# 'L 1 (#1b58a2)',
# 'U 2 (#caa171)',
# 'R 2 (#7807d2)',
# 'U 3 (#a77fa3)',
# 'L 2 (#015232)',
# 'U 2 (#7a21e3)']
# for i in range(len(lines)):
#     lines[i]=lines[i].split()
#     lines[i]=list(lines[i])
insts=[]
dmap={'0':'R','1':'D','2':'L','3':'U'}
for i in range(len(lines)):
    dxn2=dmap[lines[i][2][7]]
    dist=int(lines[i][2][2:7],16)
    insts.append((dxn2,dist))
    
#and now i have to find the area, lol
#strat
#plot only north and south walls
#this should be tractable enough...
#max complexity should be about 60m

#rays...
combomap={'UR':'F','LD':'F','RD':'7','UL':'7','RU':'J',
          'DL':'J','DR':'L','LU':'L'}
left={'UL','RU','DR','LD'} #ulru cast right else left
perim=set()
hperim,vperim=[],[]
corners=[]
pos=[0,0]
sub=0
for i in range(len(insts)):
    print(i)
    dy,dx=dxn[insts[i][0]]
    dist=insts[i][1]
    y,x=pos
    combo=insts[i][0]+insts[(i+1)%len(insts)][0]
    s=combomap[combo]
    pos=(y+dy*dist,x+dx*dist)
    if insts[i][0] in {'U','D'}:
        vperim.append((x,(y,y+dy*dist)))
    else:
        hperim.append((y,(x,x+dx*dist)))
    corners.append(pos)
    sub+=dist

tot=0
for i in range(len(corners)):
    a1,a2,b1,b2=corners[i][1],corners[i][0],corners[i-1][1],corners[i-1][0]
    x=np.array([[a2,b2],[a1,b1]])
    tot+=(np.linalg.det(x))/2

tot+=sub//2+1
print(tot)
    
    
    
    
    
    
#####################################
#####################################
#####################################
#####################################
#####################################
   
    
    
    
    
    
    
    
    #####################################
hperim.sort(key=lambda x:x[0])
vperim.sort(key=lambda x:x[0])
points=set()
hrays=set()
#cast h
distx=[]
for i in range(len(corners)):
    if corners[i][1] in left:
        y,x=corners[i][0]
        if corners[i][1] in {'UL','RU'}: #c right
            dx=1
        else:
            dx=-1
        if dx==1:
            for j in range(0,len(vperim)):
                top=max(vperim[j][1][0],vperim[j][1][1])
                bottom=min(vperim[j][1][0],vperim[j][1][1])
                if x<vperim[j][0] and bottom<=y<=top:
                    hrays.add((y,(x,vperim[j][0]),dx))
                    break
        if dx==-1:
            for j in reversed(range(0,len(vperim))):
                top=max(vperim[j][1][0],vperim[j][1][1])
                bottom=min(vperim[j][1][0],vperim[j][1][1])
                if x>vperim[j][0] and bottom<=y<=top:
                    hrays.add((y,(x,vperim[j][0]),dx))
                    break
                
        distx.append(abs(x-corners[i][0][1]))
        
        
#now cast upwards... pass through rays, but not walls!
ints=[]
vrays=set()
lz=0
for i in range(len(corners)):
    if corners[i][1] in left:
        lz+=1
        y,x=corners[i][0]
        if corners[i][1] in {'UL','LD'}: #c up
            dy=-1
        else:
            dy=1
        y+=dy
        if dy==1:
            for j in range(0,len(hperim)):
                top=max(hperim[j][1][0],hperim[j][1][1])
                bottom=min(hperim[j][1][0],hperim[j][1][1])
                if y<hperim[j][0] and bottom<=x<=top:
                    vrays.add((x,(y,hperim[j][0]),dy))
                    break
        if dy==-1:
            for j in reversed(range(0,len(hperim))):
                top=max(hperim[j][1][0],hperim[j][1][1])
                bottom=min(hperim[j][1][0],hperim[j][1][1])
                if y>hperim[j][0] and bottom<=x<=top:
                    vrays.add((x,(y,hperim[j][0]),dy))
                    break

        distx.append(abs(y-corners[i][0][0]))
#next ray intersection, this will generate the relevant points.
intx=[]
for i in hrays:
    l=min(i[1][0],i[1][1])
    r=max(i[1][0],i[1][1])
    for j in vrays:
        top=max(j[1][0],j[1][1])
        bottom=min(j[1][0],j[1][1])
        if bottom<i[0]<top and l<j[0]<r:
            intx.append((i[0],j[0]))
extra=0
for i in hrays:
    extra+=abs(i[1][1]-i[1][0])
for i in vrays:
     extra+=abs(i[1][1]-i[1][0])

#generate interesting point set... 
#will need some proof that 
points=[]
for i in vrays:
    if i[2]==-1: #dy -1 = going up
        points.append(((i[1][1],i[0]),(1,1,0,0)))
    else:
        points.append(((i[1][1],i[0]),(0,0,1,1)))
        
for i in hrays:
    if i[2]==-1: #left
        points.append(((i[0],i[1][1]),(1,0,0,1)))
    else:
        points.append(((i[0],i[1][1]),(0,1,1,0)))

for i in intx:
    points.append((i,(1,1,1,1)))


    
for i in range(len(corners)):
    t=combomap[corners[i][1]]
    if corners[i][1] in {'UL','RU','DR','LD'}: #left
        if t=='F':
            points.append((corners[i][0],(0,1,1,1)))
        elif t=='7':
            points.append((corners[i][0],(1,0,1,1)))
        elif t=='J':
            points.append((corners[i][0],(1,1,0,1)))
        else: #L
            points.append((corners[i][0],(1,1,1,0)))
    else:
        if t=='F':
            points.append((corners[i][0],(1,0,0,0)))
        elif t=='7':
            points.append((corners[i][0],(0,1,0,0)))
        elif t=='J':
            points.append((corners[i][0],(0,0,1,0)))
        else: #L
            points.append((corners[i][0],(0,0,0,1)))
        
            
                    
        
##### IT REMAINS TO TRAVERSE THE SQUARES...
#WE may traverse, iff ray/edge
#how to check if ray, hray dict(x,y)=(1,0,1,1) ideal
vdict,hdict=defaultdict(list),defaultdict(list)
for i in points:
    vdict[i[0][0]].append(i[0][1])
    hdict[i[0][1]].append(i[0][0])
for i in vdict: #key = yval
    vdict[i].sort()
for i in hdict: #key = xval
    hdict[i].sort()

def findNext(pt,dxn):
    if dxn==0: #search right
        key=pt[0]
        for i in range(len(vdict[key])):
            if vdict[key][i]==pt[1]:
                return (pt[0],vdict[key][i+1])
    elif dxn==1:
        key=pt[1]
        for i in range(len(hdict[key])):
            if hdict[key][i]==pt[0]:
                return (hdict[key][i+1],pt[1])
    elif dxn==2:
        key=pt[0]
        for i in reversed(range(len(vdict[key]))):
            if vdict[key][i]==pt[1]:
                return (pt[0],vdict[key][i-1])
    
    elif dxn==3:
        key=pt[1]
        for i in reversed(range(len(hdict[key]))):
            if hdict[key][i]==pt[0]:
                return (hdict[key][i-1],pt[1])
        

    
sqs=[]
tot=0
dxns=((0,1),(1,0),(0,-1),(-1,0))

for i in points:
    #print(i)
    base=i[0]+()
    for j in range(4): #the sq
        l=[]
        if i[1][j]==0:
            continue
        for k in range(4): #the dxn  
            print(base)
            c1,c2=base+()
            print(base) 
            base=findNext(base,(j+k)%4)
            l.append(abs(c1-base[0])+abs(c2-base[1]))
        print(l)
        sqs.append(l)
sqs2=[sorted(i) for i in sqs]
sqs2=[tuple(i) for i in sqs2]
sqs3=list(set(sqs2))     
tot=0
for i in range(len(sqs3)):
    tot+=((sqs3[i][0]-1)*(sqs3[i][2]-1))
tot2=0
for i in range(len(insts)):
    tot2+=insts[i][1]
tot+=tot2
#sum rays...
tot+=extra
print(tot) #9 too large -5 walls #-4
tot-=len(hrays)+len(intx)
# tot-=len(distx) #walls
# tot-=len(ints) #internal corners
print(tot)
#17505859279533500
#120275887427032 too low
##########
#952408144129 #me
952408144115-952403777654
 extra+=abs(i[1][1]-i[1][0])
#952408144114
#952408144115 #correct
#952408144110 out by 5 smhmh
#5 left turns - left turns add two to the area i surpose
#out by 14 - number of intersections...
sum(distx)


        
        
print(tot2)    
    
    














corners=[]
northwalls=defaultdict(list)
for i in range(len(insts)):
    print(i)
    dy,dx=dxn[insts[i][0]]
    dist=insts[i][1]
    y,x=pos
    if insts[i][0] in {'U','D'}:
        for j in range(1,dist):
            northwalls[y+dy*j].append((x,'|'))
    combo=insts[i-1][0]+insts[i][0]
    s=combomap[combo]
    northwalls[y].append((x,s))
    pos=(y+dy*dist,x+dx*dist)
    corners.append(pos)
#what goes up must come down....
  
tot=0
for i in northwalls:
    northwalls[i].sort()
    ct=0
    for j in range(1,len(northwalls[i])):
        if northwalls[i][j][1] in {'|','L','J'}:
            ct+=1 #going in 
        if ct%2==1 and northwalls[i][j][1] not in {'7','J'}:
            tot+=(northwalls[i][j][0]-northwalls[i][j-1][0])
for i in insts:
    tot+=i[1]
#inv=-356818 [219114]

#952408144115
#952403979175 they
#952401018787
#952405051397
tot2,totl,totr=0,0,0

print(totl,totr)
        

they
#952405051397

#680425388601
#952408144115 me
-952405051397
        
        
