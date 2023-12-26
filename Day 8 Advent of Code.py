#465680095962898441171337 too high...
import numpy as np
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput8.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')

dic={} 
for i in range(2,len(lines)):
    st,l,r=lines[i][:3],lines[i][7:10],lines[i][12:15]
    dic[st]=(l,r)
   
node='AAA'
count=0
nI=len(lines[0])
iL=lines[0]
mp={"L":0,"R":1}
def findDist(init):
    node=init
    count=0
    while node!='ZZZ':
        inst=mp[iL[count%nI]]
        count+=1
        node=dic[node][inst]
    return count

findDist('AAA')
###Part 2
eIA=[]
for i in range(2,len(lines)):
    if lines[i][2]=='A':
        eIA.append(lines[i][0:3])

#brute force
def findDist2(nodes):
    count=0
    if count%10**9==0:
        print(str(count//10**9)+'bill')
    ends=[nodes[i][2] for i in range(len(nodes[:1]))]
    while ends!=['Z','Z','Z','Z','Z','Z']:
        count+=1
        for i in range(len(nodes)):
            inst=mp[iL[count%nI]]
            nodes[i]=dic[nodes[i]][inst]
        ends=[nodes[i][2] for i in range(len(nodes[:1]))]
    return count

#findDist2(eIA)
#lcm method
def findDistLCM(nodes):
    nodes=nodes+[]
    arr=[]
    for i in range(len(nodes)):
        count=0
        c=[0]
        seen=0
        orig=nodes[i]
        while True:
            if orig[2]=='Z':
                c.append(count-c[-1])
                seen+=1
                if seen==2:
                    arr.append(c[1:])
                    break
            inst=mp[iL[count%nI]]
            count+=1
            orig=dic[orig][inst]
    return arr
a=findDistLCM(eIA)

print(a)
import math
mod=[i[1] for i in a]
math.lcm(*mod)
#do chinese remainder theorem... (properly)


rem=[i[0] for i in a]

np.lcm.reduce(mod)
465680095962898441171337%10371555451871

for i in mod:
    print(10371555451871%i)
10371555451871
