from copy import deepcopy
import numpy as np
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput15.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip('\n')
        lines[i]=lines[i].split(',')
lines=lines[0]
s=lines[0]
def HASH(s):
    n=0
    for i in s:
        val=ord(i)
        n+=val
        n*=17
        n%=256
    return n
    
HASH('HASH')
    
def Part1(lines):
    tot=0
    for i in range(len(lines)):
        tot+=HASH(lines[i])
    return tot
Part1(lines)
##Part 2

def Part2(lines):
    buckets=[{} for i in range(256)] #probably holding hashmaps lol
    for i in range(len(lines)):
        s=lines[i]
        if s[-1]=='-':
            symb='-'
            label=s[:-1]
        else:
            label=s[:-2]
            symb='='
        h=HASH(label)
        if symb=='=':
            buckets[h][label]=int(s[-1])
        elif symb=='-':
            if label in buckets[h]:
                buckets[h].pop(label)
    tot=0
    for i in range(len(buckets)):
        slot=1
        for j in buckets[i]:
            tot+=(i+1)*slot*buckets[i][j]
            slot+=1
    return tot
Part2(lines)
            
            
            
        
                
    
    
    



