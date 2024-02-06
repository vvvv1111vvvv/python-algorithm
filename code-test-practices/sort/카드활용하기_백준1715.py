n=int(input())
card=[]
for i in range(n):
    card.append(int(input()))
card.sort()
result=0
count=card[0]
if len(card)==1:
    result=count
    print(result)
else:
    for i in range(1,n):
        count+=card[i]
        result+=count
    print(result)