import numpy as np
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput12.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
    
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split(" ")
    lines[i][1]=lines[i][1].split(",")
    lines[i][1]=[int(_) for _ in lines[i][1]]

#? effectively wildcard
#
for i in range(len(lines)):
    blocks,ct=[],0
    for j in range(len(lines[i][0])):
        if lines[i][0][j]=='.' and ct>0:
            blocks.append(ct)
            ct=0
        else:
            ct+=1
    if ct!=0 and lines[i][0][-1]!='.':
        blocks.append(ct)
    lines[i].append(blocks)
    
#1-contiguous strings, 2 blocks, dynamic programming?
#need some dp for 
#  # #### 2 1 
#i'm afraid I might have to try RECURSION
poss=[]
def recursive(l,blocks):
    tot=0
    if blocks==[]:
        tot+=1
        return tot
    for i in range(len(l)):
        block=blocks[0]
        if  '.' not in l[i:i+block] and i+block<=len(l) and (i+block==len(l) or l[i+block]!='#'):
            if not (blocks[1:]==[] and '#' in l[i+block:]):
                tot+=recursive(l[i+block+1:],blocks[1:])
        if l[i]=='#':
            break
    return tot

recursive(lines[259][0],lines[259][1])
#need 4
top=0
for i in range(len(lines)):
    top+=recursive(lines[i][0],lines[i][1])
    print(recursive(lines[i][0],lines[i][1]))
print(top)
#testcases =2,3,6,14,22,15,14,1,5,9
#4567
v=np.array(list(lines[2][0]))

top=0 
for i in range(len(lines)):
    newline=((lines[i][0]+'?')*5)[:-1]
    v=recursive(newline,lines[i][1]*5)
    print(v)
    top+=v

print(top)

print(recursive((('?###????????'+'?')*5)[:-1], [3,2,1]*5))
#The efficiency edit.
#memoisation?- if seen before, terminate.
#this is the logic- , it works, but is too heavy
#it is possible if we have very little to fill, to fill
#???????? [1,1,1,1] on repeat will have very many fillings
#we can't really use patterns and powers, 
#part 2
cache={} #memoize if subpattern seen before
def recursive(l,blocks):
    if (l,tuple(blocks)) in cache:
        return cache[(l,tuple(blocks))]
    tot=0
    if blocks==[]:
        cache[l]=1
        tot=1
        return tot
    for i in range(len(l)):
        block=blocks[0]
        if  '.' not in l[i:i+block] and i+block<=len(l) and (i+block==len(l) or l[i+block]!='#'):
            if not (blocks[1:]==[] and '#' in l[i+block:]):
                tot+=recursive(l[i+block+1:],blocks[1:])
        if l[i]=='#':
            break
    cache[(l,tuple(blocks))]=tot
    return tot

top=0  
for i in range(len(lines)):
    top+=recursive(lines[i][0],lines[i][1])
    print(recursive(lines[i][0],lines[i][1]))
    
print(top)  
#testcases =2,3,6,14,22,15,14,1,5,9     
top=0
for i in range(len(lines)):
    newline=((lines[i][0]+'?')*5)[:-1]
    v=recursive(newline,lines[i][1]*5)
    print(v)
    top+=v
print(top)

#10103548592809 too high
#4964259839627