from copy import deepcopy
import numpy as np
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput14.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')
        lines[i]=list(lines[i])

#r1=100 etc.
grid=np.array(lines)
def tilt(lines):
    grid=[['.' for i in range(len(lines))] for j in range(len(lines[0]))]
    
    for i in range(len(lines[0])): #colfirst (north tilt)
        base=0
        for j in range(len(lines)): #depth
            
            if lines[j][i]=='O':
                grid[base][i]='O'
                base+=1
            elif lines[j][i]=='#':
                grid[j][i]='#'
                base=j+1
    return grid

v=np.array(tilt(lines))

def score(grid):
    tot=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='O':
                tot+=len(grid)-i
    return tot
score(v)

##Part 2 1b 
##
def tiltalt(grid,dxn):
    grid2=[['.' for i in range(len(lines))] for j in range(len(lines[0]))]
    if dxn=='N':
        for i in range(len(grid[0])): #colfirst (north tilt)
            base=0
            for j in range(len(grid)): #depth
                if grid[j][i]=='O':
                    grid2[base][i]='O'
                    base+=1
                elif grid[j][i]=='#':
                    grid2[j][i]='#'
                    base=j+1
    elif dxn=='S':
        for i in range(len(grid[0])): #colfirst (north tilt)
            base=len(grid)-1
            for j in reversed(range(len(grid))): #depth
                if grid[j][i]=='O':
                    grid2[base][i]='O'
                    base-=1
                elif grid[j][i]=='#':
                    grid2[j][i]='#'
                    base=j-1
    elif dxn=='W': #shift left
        for i in range(len(grid)): #colfirst (north tilt)
            base=0
            for j in range(len(grid[0])): #depth
                if grid[i][j]=='O':
                    grid2[i][base]='O'
                    base+=1
                elif grid[i][j]=='#':
                    grid2[i][j]='#'
                    base=j+1
    elif dxn=='E':
        for i in range(len(grid)): #colfirst (north tilt)
            base=len(grid[0])-1
            for j in reversed(range(len(grid[0]))): #depth
                if grid[i][j]=='O':
                    grid2[i][base]='O'
                    base-=1
                elif grid[i][j]=='#':
                    grid2[i][j]='#'
                    base=j-1
    return grid2
# lines=[
# 'OOOO.#.O..',
# 'OO..#....#',
# 'OO..O##..O',
# 'O..#.OO...',
# '........#.',
# '..#....#.#',
# '..O..#.O.O',
# '..O.......',
# '#....###..',
# '#....#....']
       
       
for i in range(len(lines)):
    lines[i]=list(lines[i])



def cycle():
    spins=('N','W','S','E')
    grid=deepcopy(lines)
    res=[]
    loop=[]
    res.append(grid)
    j=1
    for i in range(10000):
        for k in spins:
            grid=tiltalt(grid,k)
        if loop and grid==loop[0]:
            second=j-first
            return first,second,loop[0]
            print(j)
        if grid in res and loop==[]:
            first=j
            print(j)
            loop.append(grid)
        res.append(grid)
        j+=1
    s=score(grid)

f,s,loop=cycle()
def part2(cycles,f,s):
    cycles-=f
    cycles=cycles%s
    print(cycles)
    return cycles
r=part2(10**9,f,s)
#1b cycles-

def cycles(loop,r): #start of cycle
    spins=('N','W','S','E')
    grid=deepcopy(loop)
    for i in range(r):
        for k in spins:
            grid=tiltalt(grid,k)
    print(grid)
    return score(grid)

cycles(loop,r)

#95162 too low...
        
        
    
    
    #NWSE
    


