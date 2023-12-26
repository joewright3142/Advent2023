import numpy as np
from collections import deque

filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput10.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=list(lines[i])
    
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=='S':
            s=(i,j)
            

v=np.array(lines)
#cases
def findS(s):
    a=[]
    i,j=s
    if i>0 and lines[i-1][j] in {'|','F','7'}:
        a.append({'|','L','J'})
    if i<len(lines)-1 and lines[i+1][j] in {'|','L','J'}:
        a.append({'|','F','7'})
    if j>0 and lines[i][j-1] in {'-','F','L'}:
        a.append({'-','J','7'})
    if j<len(lines[0])-1 and lines[i][j+1] in {'-','J','7'}:
        a.append({'-','F','L'})
    return a[0].intersection(a[1]).pop()

lines[s[0]][s[1]]=findS(s)
uc={'|','F','7'}
dc={'|','L','J'}
lc={'-','J','7'}
rc={'-','F','L'}

#if pos=F and prev=up
#returns next dir
dic={'F':((1,0),(0,1)) #down or right
      ,'-':((0,-1),(0,1)) #lr
      ,'|':((1,0),(-1,0))
      ,'L':((-1,0),(0,1))
      ,'J':((-1,0),(0,-1))
      ,'7':((1,0),(0,-1))
     }


def findLL(s):
    dirs=((1,0),(-1,0),(0,1),(0,-1))
    isvis=set()
    if lines[s[0]][s[1]] in dc:
        dxn=(-1,0)
    elif lines[s[0]][s[1]] in uc:
        dxn=(1,0)
    else:
        dxn=(0,1)
    nxt=(s[0]+dxn[0],s[1]+dxn[1])
    isvis.add(s)
    pos=nxt
    steps=2 #2 since the first step done, last will not be completed
    n=len(lines)
    while steps==0 or pos!=s:
        pos=nxt
        ct=0
        symbol=lines[pos[0]][pos[1]]
        for i in dic[symbol]:
            if (pos[0]+i[0],pos[1]+i[1]) not in isvis:
                nxt=(pos[0]+i[0],pos[1]+i[1])
                steps+=1
                isvis.add(pos)
                ct+=1
        if ct==0:
            isvis.add(pos)
            break
                
    return steps/2,isvis

findLL(s)[0]

#Part 2
#test 
# lines=[
# '..........',
# '.F------7.',
# '.|F----7|.',
# '.||....||.',
# '.||....||.',
# '.|L-7F-J|.',
# '.|..||..|.',
# '.L--JL--J.',
# '..........',
# '..........']

r=findLL(s)[1]
for i in range(len(lines)):
    for j in range(len(lines)):
        if (i,j) not in r:
            lines[i][j]='.'
    

v=np.array(lines)
v2=np.zeros((len(lines),len(lines)))
tot=0
for i in range(len(lines)):
    ct=0
    for j in range(len(lines[0])):
        if lines[i][j] in {'|','L','J'}:
            ct+=1
        if ct%2==1 and lines[i][j]=='.':
            tot+=1
            v2[i][j]=ct
            
    

vt={"7F","7L","7|"
"|L","||","|F"
,"JL","J|","JF"}

hz={"7F","7L", "7-",
"-L","--","-F","JL","J-","JF"}

#Everything reachable from (0,0) is outside
def Paint(source):
    newgrid=grid+0
    newgrid[source[0]][source[1]]=2
    n=len(lines)
    q=deque([source])
    #when can we go through something... #if already on a border
    isvis={source}
    dirs=((1,0),(-1,0),(0,1),(0,-1))
    while q:
        y,x=q.popleft()
        newgrid[y][x]=2
        for dy,dx in dirs:
            flag=0
            if 0<=x+dx<n and 0<=y+dy<n and (y+dy,x+dx) not in isvis:
                if (lines[y][x]=='-' and dy!=0) or (lines[y][x]=='|' and dx!=0):
                    continue
                if lines[y+dy][x+dx]!='.':
                    if dy!=0:
                        p=lines[y+dy][x+dx]+lines[y+dy][x+dx+1]
                        if p not in vt:
                            flag=1
                    if dx!=0:
                        p=lines[y+dy][x+dx]+lines[y+dy-1][x+dx]
                        if p not in hz:
                            flag=1
                if flag==0:
                    if (y+dy,x+dx) not in isvis:
                        isvis.add((y+dy,x+dx))
                        q.append((y+dy,x+dx))
    return newgrid
                    
new=Paint((0,0))
tot=0
for i in range(len(new)):
    for j in range(len(new)):
        if new[i][j]==0:
            tot+=1
            












def Paint(source):
    newgrid=grid+0
    newgrid[source[0]][source[1]]=2
    n=len(lines)
    q=deque([source])
    #when can we go through something... #if already on a border
    isvis={source}
    dirs=((1,0),(-1,0),(0,1),(0,-1))
    while q:
        y,x=q.popleft()
        newgrid[y][x]=2
        for dy,dx in dirs:
            if 0<=x+dx<n and 0<=y+dy<n and (y+dy,x+dx) not in isvis:
                if (y+dy,x+dx)==(6,4):
                    print(y,x) 
                if (lines[y+dy][x+dx]== '-' or lines[y][x] in symbsv) and dy!=0: #on a border, trying to move in
                    if (y+dy,x+dx)==(6,4):
                        print(dy,dx)
                        print("b1")
                        print(y,x)
                    continue
                elif (lines[y+dy][x+dx]== '|' or lines[y][x] in symbsa) and dx!=0: #on a border, trying to move in
                    if (y+dy,x+dx)==(6,4):
                        print('b2')
                        print(y,x)
                    continue
                else:
                    if (y+dy,x+dx) not in isvis:
                        isvis.add((y+dy,x+dx))
                        q.append((y+dy,x+dx))
    return newgrid



                
                
            

    

                
            
        
    

        
    