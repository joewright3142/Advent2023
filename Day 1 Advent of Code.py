filepath=r'C:\Users\cege\Desktop\ACinput.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')

#Part 1
tot=0
for i in lines:
    num=""
    for j in i:
        if j.isnumeric():
            num+=j
            break
    for j in i[::-1]:
        if j.isnumeric():
            num+=j
            break
    tot+=int(num)

#Part 2
find=["one","two","three","four","five","six","seven","eight","nine"
      ,"1","2","3","4","5","6","7","8","9"]
convert={"one":"1","two":"2","three":"3",
         "four":"4","five":"5","six":"6"
         ,"seven":"7","eight":"8","nine":"9"}

tot=0
for i in range(len(lines)):
    l=[]
    for j in range(len(find)):
        s=find[j]
        v=lines[i].find(s)
        if v!=-1:
            if not s.isnumeric():
                l.append((v,int(convert[s])))
            else:
                l.append((v,int(s)))
    l.sort(key=lambda x:x[0])
    score=l[0][1]*10
    l2=lines[i][::-1]
    l=[]
    for j in range(len(find)):
        s=find[j][::-1]
        v=l2.find(s)
        if v!=-1:
            if not s.isnumeric():
                l.append((v,int(convert[s[::-1]])))
            else:
                l.append((v,int(s)))
    l.sort(key=lambda x:x[0])
    score+=l[0][1]
    print(score)
    tot+=score
            

##########
         

            
            
    
