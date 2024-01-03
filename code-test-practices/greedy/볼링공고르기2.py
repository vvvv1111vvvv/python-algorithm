n,m= map(int, input().split())
data=list(map(int,  input().split()))
w=[0]*(m+1)
result=0
#for i in range(1,len(w)):
#    w[i]=data.count(i)
#passed=w[1]
#for i in range(1, len(w)-1):
#    result+=w[i]*(n-passed)
#    passed+=w[i+1]
#print(result)
for x in data:
    w[x]+=1
for i in range(1, m+1):
    n-=w[i]
    result+=w[i]*n
print(result)