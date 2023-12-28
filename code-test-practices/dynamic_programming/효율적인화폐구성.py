n,m=map(int, input().split())
moneys=[]
#d=[0]*10001
#d[1]=m
count=0
for _ in range(n):
    moneys.append(int(input()))
d=[10001]*(m+1)
d[0]=0
for money in moneys:
    for j in range(money, m+1):
        if d[j-money]!= 10001:
            d[j]= min(d[j],d[j-money]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])
        