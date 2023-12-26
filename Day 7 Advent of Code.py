filepath=r'C:\Users\cege\Documents\GitHub\Advent2023\ACinput7.txt'
with open(filepath,'r') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip('\n')
    lines[i]=lines[i].split(" ")    

#who beats who?
#ranks- hc->1 1p->2 2p->3 3oK->5 4oK->6 5oK->7
h='KKAA2'
cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
def hand(h):
    nums=[]
    for i in cards:
        nums.append(h.count(i))
    if 5 in nums:
        return 7
    elif 4 in nums:
        return 6
    elif 3 in nums and 2 in nums:
        return 5
    elif 3 in nums:
        return 4
    elif nums.count(2)==2:
        return 3
    elif nums.count(2)==1:
        return 2
    else:
        return 1

for i in range(len(lines)):
    lines[i].append(hand(lines[i][0]))
#now need to do tiebreak
def score(h):
    s=0
    for i in range(len(h)):
        s+=dic[h[i]]*13**(len(h)-i-1)
    return s
     
        
    
dic={cards[i]:i for i in range(len(cards))}
for i in range(len(lines)):
    lines[i].append(score(lines[i][0]))
lines.sort(key=lambda x:(x[2],x[3]))
tot=0
for i in range(len(lines)):
    tot+=(i+1)*int(lines[i][1])

####Part 2####
for i in range(len(lines)):
    lines[i]=lines[i][:2]
cards=['J','2','3','4','5','6','7','8','9','T','Q','K','A']
dic={cards[i]:i for i in range(len(cards))}

lines[i]
def hand2(h):
    nums,origs=[],[]
    J=h.count('J')
    nums.append(J)
    origs.append(J)
    for i in cards[1:]:
        nums.append(h.count(i)+J)
        origs.append(h.count(i))
    if 5 in nums:
        return 7
    elif 4 in nums:
        return 6
    elif (J==1 and origs.count(2)==2) or (3 in origs and 2 in origs):
        return 5
    elif 3 in nums:
        return 4
    elif origs.count(2)==2:
        return 3
    elif (origs.count(2)==0 and J==1) or origs.count(2)==1:
        return 2
    else:
        return 1
h='JJABC' #can't make 2 pairs with a wildcard
hand2(h)
for i in range(len(lines)):
    lines[i].append(hand2(lines[i][0]))


dic={cards[i]:i for i in range(len(cards))}
for i in range(len(lines)):
    lines[i].append(score(lines[i][0]))
lines.sort(key=lambda x:(x[2],x[3]))
tot=0
for i in range(len(lines)):
    tot+=(i+1)*int(lines[i][1])

#248846622 too high
#248654842 too low.....
#248781813

