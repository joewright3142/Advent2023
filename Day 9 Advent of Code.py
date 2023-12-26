import numpy as np
from scipy import special
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput9.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split(" ")
    for j in range(len(lines[i])):
        lines[i][j]=int(lines[i][j])


poly=[0 for i in range(len(v))]
diffs=[v]
def diffarr(arr):
    diff=[]
    for i in range(1,len(arr)):
        diff.append(arr[i]-arr[i-1])
    if diff!=[0 for i in range(1,len(arr))]:
        diffs.append(diff)
        diffarr(diff)
diffarr(v)

tot=0
for i in range(len(lines)):
    v=lines[i]
    diffs=[v]
    diffarr(v)
    for j in range(len(diffs)-1,-1,-1):
        diffs[j-1].append(diffs[j-1][-1]+diffs[j][-1])
    tot+=diffs[0][-1]
    
###Part 2
tot=0
for i in range(len(lines)):
    v=lines[i]
    diffs=[v]
    diffarr(v)
    for j in range(len(diffs)-1,0,-1):
        diffs[j-1]=[diffs[j-1][0]-diffs[j][0]]+diffs[j-1]
    tot+=diffs[0][0]
    
#develop the polynomial


def polynomial(n): #return array with poly coeffs
    pyramid=[]
    for i in range(n+1):
        line=[j**i for j in range(1,i+2)]
        pyramid.append(line)
    coeffs=[[0 for _ in pyramid[i]] for i in range(len(pyramid))]
    #i=j=0
    for i in range(len(pyramid)): #specific power 0 high
        for j in range(len(pyramid[-i-1])): #specific coefficent in solve
            line=pyramid[-i-1][:len(pyramid[-i-1])-j]
            arr=[]
            for k in range(len(line)):
                pm=(-1)**k
                bic=special.binom(len(line)-1,k)
                arr.append(pm*bic*line[-k-1]) 
            coeffs[j+i][i]=sum(arr)
    return coeffs

def diffarr(arr):
    diffs=[arr]
    def drill(arr):
        diff=[]
        for i in range(1,len(arr)):
            diff.append(arr[i]-arr[i-1])
        if diff!=[0 for i in range(1,len(arr))]:
            diffs.append(diff)
            drill(diff)
    drill(arr)
    return diffs


def solver(seq):
    diffs=diffarr(seq)
    pynml=[0 for i in range(len(diffs))]
    eqns=polynomial(len(diffs)-1)
    for i in range(len(eqns)): 
        const=diffs[-i-1][0]
        for j in range(i):
            const-=(eqns[i][j]*pynml[j])
        const=const/eqns[i][i] 
        pynml[i]=const
    return pynml

seq=lines[0]
# for i in range(len(lines)):
#     solver(lines[i])
#     print(i)

pynml=solver(lines[0])

for i in range(1,23):
    s=0
    for j in range(len(pynml)):
        s+=pynml[j]*(i**(len(pynml)-j-1))
#A polynomial fitting the series is:
    
def FrontEnd(arr,b):
    pynml=solver(arr)
    l=[]
    for i in range(1,b+1):
        s=0
        for j in range(len(pynml)):
            s+=pynml[j]*(i**(len(pynml)-j-1))
        l.append(round(s,5))
    s=""
    lt=len(pynml)
    for i in range(lt):
        n=round(pynml[i],5)
        if n>=0:
            n="+"+str(round(pynml[i],5))
        else:
            n="-"+str(round(pynml[i],5))[1:]
        if i<lt-2:
            s+=n+'n^'+str(len(pynml)-i-1)
        elif i==lt-2:
            s+=n+'n'
        else:
            s+=n
    if s[0]=="+":
        s=s[1:]

        
    print('A polynomial fitting this sequence is: '+s)
    print("The first "+ str(b) +" terms of this sequence are: ")
    print(l)
    
def UserInput():
    a=input("Enter some numbers, (space separated)  ")
    b=input("How many terms of the sequence would you like to see?  ")
    arr=a.split()
    arr=[int(_) for _ in arr]
    b=int(b)
    FrontEnd(arr,b)

UserInput()
