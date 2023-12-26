from copy import deepcopy
import numpy as np
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput13.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')


cases,sub=[],[]
for i in range(len(lines)):
    if lines[i]!='':
        sub.append(lines[i])
    else:
        cases.append(sub)
        sub=[]
cases.append(sub)

#enumerate bitmap #=0,#=1
# for i in range(len(cases)):
def enum(case): #return vert/horiz line
    v,h=[],[]
    for i in range(len(case)): #r
        n=0
        for j in range(len(case[0])):
            if case[i][j]=='#':
                n+=2**j
        h.append(n)
    for i in range(len(case[0])): #c
        n=0
        for j in range(len(case)): #r
            if case[j][i]=='#':
                n+=2**j
        v.append(n)
    return v,h

enum(case)
        
case=cases[4]
def part1(case): #return 
    v,h=enum(case)
    #check reflection
    for i in range(1,len(v)):
        dist=min(i,len(v)-i)
        l1=v[i-dist:i]
        l2=v[i:i+dist][::-1]
        if l1==l2:
            return i
        #print(v[i-dist:i],v[i:i+dist][::-1])
    for i in range(1,len(h)):
        dist=min(i,len(h)-i)
        l1=h[i-dist:i]
        l2=h[i:i+dist][::-1]
        if l1==l2:
            return 100*i
tot=0
origline=[]
for i in range(len(cases)):
    case=cases[i]

    t=part1(case)
    if t%100==0:
        origline.append((t//100,0)) #H
    else:
        origline.append((t,1)) #V
    tot+=t

#35908 too high
#31156 too low
###part 2- adjust part 1
def part1Alt(case,dif): #return 
    v,h=enum(case)
    #check reflection
    for i in range(1,len(v)):
        dist=min(i,len(v)-i)
        l1=v[i-dist:i]
        l2=v[i:i+dist][::-1]
        if l1==l2 and i!=dif:
            return i
        #print(v[i-dist:i],v[i:i+dist][::-1])
    for i in range(1,len(h)):
        dist=min(i,len(h)-i)
        l1=h[i-dist:i]
        l2=h[i:i+dist][::-1]
        if l1==l2 and 100*i!=dif:
            return 100*i

for i in range(len(cases)):
    for j in range(len(cases[i])):
        cases[i][j]=list(cases[i][j])
#for case[1] 900 works
v=np.array(cases[1])

def part2(case):
    case=deepcopy(case)

    d=part1(case)
    

    print(r1)
    for i in range(len(case)): #r
        for j in range(len(case[0])): #c
            if case[i][j]=='#':
                case[i][j]='.'
            else:
                case[i][j]='#'
            r2=part1Alt(case,d)
            if r2 and r2!=d:
                print(i,j,r2)
                return r2
            if case[i][j]=='#':
                case[i][j]='.'
            else:
                case[i][j]='#'
    
tot=0

for i in range(len(cases)):
    case=cases[i]
    t=part2(case)
    print(t)
    tot+=t            
    
#31668- too low
#31768
        
    
    
    
    