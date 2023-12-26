import numpy
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput3.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
arr=[]
for i in lines:
    arr.append(list(i))
v=numpy.array(arr)

s={'.','0','1','2','3','4','5','6','7','8','9'}
tot=0
dirs=[(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]

for i in range(len(lines)):
    isvis=set()
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric() and j not in isvis:
            flag,n,st=0,"",0
            while j<len(lines) and lines[i][j].isnumeric():
                for dx,dy in dirs:
                    if 0<=i+dy<len(lines) and 0<=j+dx<len(lines[0]):
                        if lines[i+dy][j+dx] not in s:
                            flag=1
                n+=lines[i][j]
                j+=1
                st=1
                isvis.add(j)
            if flag:
                print(int(n))
                tot+=int(n)
                            
#part 2
tot=[]
for i in range(len(lines)):
    isvis=set()
    for j in range(len(lines[i])):
        if lines[i][j]=='*':
            nums=[]
            ct=0
            jind=j+0
            for dx,dy in dirs:
                j=jind
                if 0<=i+dy<len(lines) and 0<=j+dx<len(lines[0]):
                    if lines[i+dy][j+dx].isnumeric() and (i+dy,j+dx) not in isvis:
                        n=""
                        while j+dx>=0 and lines[i+dy][j+dx].isnumeric():
                            j-=1
                        j+=1
                        
                        while 0<=j+dx<len(lines) and lines[i+dy][j+dx].isnumeric():
                            n+=lines[i+dy][j+dx]
                            j+=1
                            isvis.add((i+dy,j+dx))
                        nums.append(n)
                        ct+=1
            if ct==2:
                tot.append(nums)

gtot=0
for i in tot:
    gtot+=int(i[0])*int(i[1])     