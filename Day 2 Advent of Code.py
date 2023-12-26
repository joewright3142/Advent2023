filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput2.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')

for i in range(len(lines)):
    lines[i]=lines[i].split(": ")[1]
    lines[i]=lines[i].split("; ")
    for j in range(len(lines[i])):
        lines[i][j]=lines[i][j].split(", ")
        for k in range(len(lines[i][j])):
            lines[i][j][k]=lines[i][j][k].split(" ")
            
    
#parameters 12r 13g 14b


def isPossible(r,g,b):
    truth=[]
    for i in range(len(lines)): #each game
        flag=1
        for j in range(len(lines[i])): #each set of experiments
            for k in range(len(lines[i][j])): #each colour
                if lines[i][j][k][1]=='blue':
                    if int(lines[i][j][k][0])>b:
                         flag=0
                elif lines[i][j][k][1]=='green':
                    if int(lines[i][j][k][0])>g:
                        flag=0 
                else:
                    if int(lines[i][j][k][0])>r:
                        flag=0 
        truth.append(flag*(i+1))
    return truth

v=isPossible(12,13,14)
sum(v)
                
def maxes():
    cubes=[]
    for i in range(len(lines)): #each game
        bmax,gmax,rmax=0,0,0
        for j in range(len(lines[i])): #each set of experiments
            for k in range(len(lines[i][j])): #each colour
                if lines[i][j][k][1]=='blue':
                    bmax=max(bmax,int(lines[i][j][k][0]))
                elif lines[i][j][k][1]=='green':
                    gmax=max(gmax,int(lines[i][j][k][0]))
                else:
                    rmax=max(rmax,int(lines[i][j][k][0]))
        print(bmax,gmax,rmax)
        cubes.append(bmax*gmax*rmax)
    return cubes
r=maxes()
sum(r)