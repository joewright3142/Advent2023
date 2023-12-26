filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput11.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=list(lines[i])
    
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i][j]=='.':
            lines[i][j]=0
        else:
            lines[i][j]=1
insert=[]
            
for i in range(len(lines)):
    if sum(lines[i])==0:
        insert.append(i)
    
newlines=[]  
for i in range(len(lines)):
    newlines.append(lines[i])
    if i in insert:
        newlines.append(lines[i])
        
insert2=[]
for i in range(len(newlines[0])): #col
    t=0
    for j in range(len(newlines)): #row
        t+=newlines[j][i]
    if t==0:
        insert2.append(i)

newlines2=[]
for i in range(len(newlines)): #row
    newlines2.append([])
    for j in range(len(newlines[0])): #col
        newlines2[i].append(newlines[i][j])
        if j in insert2:
            newlines2[i].append(newlines[i][j])

#now to find the distance btw all points

def part1(lines):
    pts=[]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]==1:
                pts.append((i,j))
    tot=0
    for i in range(len(pts)):
        for j in range(i):
            y1,x1=pts[i]
            y2,x2=pts[j]
            tot+=(abs(x1-x2)+abs(y1-y2))
    return tot

part1(newlines2)
            
#Part 2:
    
def part2(lines):
    pts=[]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]==1:
                pts.append((i,j))
    tot=0
    for i in range(len(pts)):
        for j in range(i):
            y1,x1=pts[i]
            y2,x2=pts[j]
            sub1,sub2=0,0
            for k in insert: #vertical
                if y1<k<y2 or y2<k<y1: #
                    sub1+=999999
            for k in insert2: #horizontal
                if x1<k<x2 or x2<k<x1: 
                    sub2+=999999
                
            tot+=(abs(x1-x2)+abs(y1-y2))
            tot+=sub1
            tot+=sub2

    return tot

part2(lines)

#150187313550 too low
#611998089572
