import math
filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput5.txt'
with open(filepath,'r') as f:
    lines=f.readlines()


for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
  
lines2=[]
arr=[]
for i in range(len(lines)):
    if lines[i]!="":
        arr.append(lines[i].split(" "))
    elif lines[i]=="":
        lines2.append(arr)
        arr=[]
lines2.append(arr)


seeds=[int(_) for _ in lines2[0][0][1:]]

for i in range(1,len(lines2)):
    for j in range(1,len(lines2[i])):
        for k in range(len(lines2[i][j])):
            lines2[i][j][k]=int(lines2[i][j][k])
finalLoc=[]
for s in seeds:       
    for i in range(1,len(lines2)):
        for j in range(1,len(lines2[i])):
            st,end=lines2[i][j][1],lines2[i][j][1]+lines2[i][j][2]
            newst=lines2[i][j][0]
            if st<=s<end:
                s=newst+(s-st)
                break
    finalLoc.append(s)
    
###########Part 2 unoptimised
mills=-1
mini=10**15
for s2 in range(0,len(seeds),2):
    print(s2)
    for s in range(seeds[s2],seeds[s2]+seeds[s2+1]):
        if (s-seeds[s2])%10**6==0:
            mills+=1
            print(str(mills)+"mill")
        for i in range(1,len(lines2)):
            for j in range(1,len(lines2[i])):
                st,end=lines2[i][j][1],lines2[i][j][1]+lines2[i][j][2]
                newst=lines2[i][j][0]
                if st<=s<end:
                    s=newst+(s-st)
                    break
        mini=min(s,mini)
        

print(min(finalLoc)) 
#Part2:

intervals=[(seeds[_],seeds[_]+seeds[_+1]) for _ in range(0,len(seeds),2)]
for i in intervals:
    print(i[1]-i[0])
iL=lines2+[]
for i in range(len(lines2)):
    iL[i]=iL[i][1:]
    for j in range(len(iL[i])):
        newst=iL[i][j][0]
        iL[i][j]=(iL[i][j][1],iL[i][j][1]+iL[i][j][2],-(newst-iL[i][j][1]))
    iL[i].sort(key=lambda x:x[0])
iL[0]=sorted(intervals,key=lambda x:x[0])

#Make intervals dense
for i in range(1,len(iL)):
    for j in range(len(iL[i])-1):
        if iL[i][j][1]!=iL[i][j+1][0]:
            iL[i].append((iL[i][j][1],iL[i][j+1][0],0))
    iL[i].sort(key=lambda x:x[0])
    iL[i]=[(-math.inf,iL[i][0][0],0)]+iL[i]+[(iL[i][-1][1],math.inf,0)]         
    


#next
nxt=iL[0]
for i in range(1,len(iL)):
    print(len(nxt))
    nxt2=[]
    for iv in nxt:
        flag=0
        for j in range(len(iL[i])): #all intervals...
            if iL[i][j][0]<=iv[0]<iL[i][j][1] and iv[1]<iL[i][j][1]:
                flag=1
                st=end=0
                n=iL[i][j][2]
                nxt2.append((iv[0]-n,iv[1]-n)) 
                break
            if iL[i][j][0]<=iv[0]<iL[i][j][1]: #starter bucket
                st=j
                nst=iL[i][j][2]
            if iL[i][j][0]<=iv[1]<iL[i][j][1]: #end bucket
                end=j
                nend=iL[i][j][2]
        if flag==0:
            for k in range(st+1,end):
                n=iL[i][k][2]
                nxt2.append((iL[i][k][0]-n,iL[i][k][1]-n))
            nxt2.append((iv[0]-nst,iL[i][st][1]-nst))
            nxt2.append((iL[i][end][0]-nend,iv[1]-nend))
    print(nxt)
    nxt=nxt2
            
nxt.sort(key=lambda x:x[0])             
print(nxt[0][0])
            
#1281980084 too high




    