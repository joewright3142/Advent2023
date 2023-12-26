filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput4.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split(": ")[1]
    lines[i]=lines[i].split(' | ')
    for j in range(len(lines[i])):
        lines[i][j]=lines[i][j].split(" ")
        lines[i][j].sort(reverse=True)
        while lines[i][j][-1]=="":
            lines[i][j].pop()
tot=0
arr=[1 for i in range(len(lines))]
for i in range(len(lines)):
    s=0
    for j in lines[i][1]:
        if j in lines[i][0]:
            s+=1
    print(s)
    if s>=1:
        tot+=2**(s-1)
####

tot=0
arr=[1 for i in range(len(lines))]
for i in range(len(lines)):
    s=0
    for j in lines[i][1]:
        if j in lines[i][0]:
            s+=1
    for j in range(s):
        arr[i+j+1]+=arr[i]

sum(arr)

