from copy import deepcopy
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput20.txt'
import math
res=math.inf
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    
class flipflop():
    def __init__(self,children,state=0):
        self.children=children
        self.state=state
    def applyPulse(self,pulse):
        if pulse==1: #high pulse
            return
        elif pulse==0: #low pulse
            self.state=(self.state+1)%2
            for i in self.children:
                q.append((i,self.state,u[0])) #outgoing pulse
        return self.state #the new pulse.
class broadcaster():
    def __init__(self,children):
        self.children=children
    def applyPulse(self):
        for i in self.children:
            q.append((i,0,u[0])) #always sends a low pulse
            
class conjunction():
    def __init__(self,children,parents):
        self.children=children #[a,b,c]
        self.parents=parents
        self.pulses={i:0 for i in parents}
        #initialise low pulses
    def applyPulse(self,inp):
        self.pulses[inp[2]]=inp[1]
        p=min(self.pulses.values())
        for i in self.children:
            q.append((i,(p+1)%2,u[0]))
        return p
        
##Now for the parsing. - create broadcaster,flipflop and conjunctions
######TEST####
# lines=[
# 'broadcaster -> aa, bb, cc',
# '%aa -> bb',
# '%bb -> cc',
# '%cc -> in',
# '&in -> aa']

# lines=[
# 'broadcaster -> aa',
# '%aa -> in, co',
# '&in -> bb',
# '%bb -> co',
# '&co -> ou']
variables={}
for i in range(len(lines)):
    if lines[i][0]=='b': #broadcaster
        c=lines[i][15:]
        c=c.split(', ')
        name=lines[i][0:3]
        variables[name]=broadcaster(c)
    if lines[i][0]=='%': #flip 
        c=lines[i][7:]
        c=c.split(', ')
        #now find p.
        name=lines[i][1:3]
        variables[name]=flipflop(c)
    
    if lines[i][0]=='&': #conjunction
        c=lines[i][7:]
        c=c.split(', ')
        #now find p.
        name=lines[i][1:3]
        p=[]
        for j in range(len(lines)):
            if lines[j][0]!='b': #we don't cast to broadcaster
                if name in lines[j][3:]:
                    p.append(lines[j][1:3])
        variables[name]=conjunction(c,p)
        
#outputs

def part1(pushes):
    #start with broadcast
    pcount=[0,0]
    pushes=1000
    for i in range(pushes):

        q=deque([('bro',0,'button')])
        while q:
            u=q.popleft()
            #print(u[2],u[1],u[0])
            pcount[u[1]]+=1
            if u[0] not in variables: #exit
                continue
            var=variables[u[0]]
            if type(var)==broadcaster:
                var.applyPulse()
            elif type(var)==flipflop:
                var.applyPulse(u[1])
            elif type(var)==conjunction:
                var.applyPulse((u[0],u[1],u[2]))
    return pcount

pcount[0]*pcount[1]
            
part1(1000)
####  
#1b too low
pcount=[0,0]
pushes=1000000000000
lcm=set()
seen={}
for i in range(1,pushes):
    if len(lcm)==4:
        break
    q=deque([('bro',0,'button')])
    while q:
        u=q.popleft()
        #print(u[2],u[1],u[0])
        pcount[u[1]]+=1
        if u[2] in {'xn','qn','xf','zl'} and u[1]==1:
            
            if u[2] not in seen:
                lcm.add(i)
            seen[u[2]]=i
            
            
               
                
        if u[0] not in variables: #exit
            continue
        var=variables[u[0]]
        if type(var)==broadcaster:
            var.applyPulse()
        elif type(var)==flipflop:
            var.applyPulse(u[1])
        elif type(var)==conjunction:
            var.applyPulse((u[0],u[1],u[2]))
#brute force not gonna work...
#reverse engineer:
    
from math import gcd
   #will work for an int array of any length
lcm2 = 1
for i in lcm:
    lcm2 = lcm2*i//gcd(lcm2, i)
print(lcm2)
#220263287915239
#224046542165867
#from copy import deepcopy
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput20.txt'
{3793, 3923, 3739, 4027}