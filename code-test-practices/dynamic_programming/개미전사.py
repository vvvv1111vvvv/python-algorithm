n=int(input())
data=list(map(int, input().split()))
d=[0]*101
d[2]=max(data[1], data[0])
d[3]=max(data[0]+data[2], data[1])
for i in range(4,n+1):
    d[i]=max(d[i-1], d[i-2]+data[i-1])
print(d[n])