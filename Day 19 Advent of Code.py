from copy import deepcopy
import heapq 
import numpy as np
from collections import deque
from collections import defaultdict
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput19.txt'

with open(filepath,'r') as f:
    lines=f.readlines()
    
# lines=[
# 'px{a<2006:qkq,m>2090:A,rfg}',
# 'pv{a>1716:R,A}',
# 'lnx{m>1548:A,A}',
# 'rfg{s<537:gd,x>2440:R,A}',
# 'qs{s>3448:A,lnx}',
# 'qkq{x<1416:A,crn}',
# 'crn{x>2662:A,R}',
# 'in{s<1351:px,qqz}',
# 'qqz{s>2770:qs,m<1801:hdj,R}',
# 'gd{a>3333:R,R}',
# 'hdj{m>838:A,pv}',
# '',
# '{x=787,m=2655,a=1222,s=2876}',
# '{x=1679,m=44,a=2067,s=496}',
# '{x=2036,m=264,a=79,s=2244}',
# '{x=2461,m=1339,a=466,s=291}',
# '{x=2127,m=1623,a=2188,s=1013}'] 
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    if lines[i]=="":
        idx=i
rules=lines[:idx]
parts=lines[idx+1:]
       

for i in range(len(rules)):
    rules[i]=rules[i].split('{')
    rules[i][1]=rules[i][1].split(',')
    rules[i][1][-1]=rules[i][1][-1][:-1]
    for j in range(len(rules[i][1])-1):
        rules[i][1][j]=rules[i][1][j].split(':')
rulesdic={}

for i in rules:
    rulesdic[i[0]]=i[1:][0]
rulesdic['A']=1
rulesdic['R']=0
#Write a function assigning it to workflow...
ps=[] 
for i in range(len(parts)):
    parts[i]=parts[i].split('=')
    s=[]
    for j in range(1,len(parts[i])):
        s.append(parts[i][j].split(",")[0])
    s[-1]=s[-1][:-1]
    s=[int(i) for i in s]
    ps.append(s)

intmap={0:'x',1:'m',2:'a',3:'s'}
lmap={'x':0,'m':1,'a':2,'s':3}

pos='in'
def part1(ps,rulesdic):
    tot=0
    for j in range(len(ps)):
        pos='in'
        part=ps[j]
        while pos not in {'A','R'}:
            print(pos)
            for i in rulesdic[pos]:
                if type(i)==list:
                    l=i[0][0]
                    s=i[0][1]
                    n=int(i[0][2:])
                    idx=lmap[l]
                    partn=int(ps[j][idx])
                    if (s=='>' and partn>n) or (s=='<' and partn<n):
                        pos=i[1]
                        break
                else:
                    pos=i
        tot+=rulesdic[pos]*sum(ps[j])
    return tot
                
part1(ps,rulesdic)
#######part 2, combinations####
#partiony boi
#send intervals down pipelines...
#every point has exactly one flow.
#intvls (xmas)
def cutPass(intvl,n,s):
    st,en=intvl[0],intvl[1]
    if n>en:
        if s=='<':
            return intvl,(-1,-1)
        elif s=='>':
            return (-1,-1),intvl
    if n<st:
        if s=='<':
            return (-1,-1),intvl
        elif s=='>':
            return intvl,(-1,-1)
    if s=='>':
        c=(n+1,en)
        p=(st,n)

    elif s=='<':
        c=(st,n-1)
        p=(n,en)
    
    return c,p
    
cutPass((0,9999),1000,'>')
    
def recursive(intvls,pos):  
    if (-1,-1) in intvls:
        return
    if pos in ('A','R'):
        if pos=='A':
            res.append(intvls)
        if pos=='R':
            res2.append(intvls)
        return
    for i in rulesdic[pos]:
        if type(i)==list:
            l=i[0][0]
            s=i[0][1]
            n=int(i[0][2:])
            idx=lmap[l]
            c,p=cutPass(intvls[idx],n,s)
            cut=deepcopy(intvls)
            cut[idx]=c
            Pass=deepcopy(intvls)
            Pass[idx]=p
            print(cut,Pass)
            recursive(cut,i[1]) #drilldown
            intvls=Pass
        else:
            pos=i
            recursive(Pass,i)
        
test=[(1,4000),(1,4000),(1,4000),(1,4000)]   
pos='in'   

res=[]
res2=[]
recursive(test,pos)
#issue, getting overlap!
tot=0   
for i in res:
    l=1
    for j in range(4):
        l*=(1+i[j][1]-i[j][0])
    tot+=l
print(tot)
for i in res2:
    l=1
    for j in range(4):
        l*=(1+i[j][1]-i[j][0])
    tot+=l
print(tot)

#likely slightly out in cutpass
#167578630387434 me 
#167409079868000 they
167578630387434-167409079868000
    
    
    