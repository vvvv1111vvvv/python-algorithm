from itertools import permutations
n= int(input())
d=list(map(int, input().split()))
temp_oper=list(map(int, input().split()))
oper=[]
for i in range(4):
    if temp_oper[i]!=0:
        oper+=[i]*temp_oper[i]
oper=set(tuple(permutations(oper,n-1)))
max_val=-int(1e9)
min_val=int(1e9)
for i in range(len(oper)):
    mid_result=d[0]
    now=oper.pop()
    for j in range(n-1):
        if now[j]==0:
            mid_result+=d[j+1]
        elif now[j]==1:
            mid_result-=d[j+1]
        elif now[j]==2:
            mid_result*=d[j+1]
        elif now[j]==3:
            if mid_result<0:
                mid_result=-(abs(mid_result)//d[j+1])
            else:
                mid_result=mid_result//d[j+1]
    max_val=max(max_val, mid_result)
    min_val=min(min_val, mid_result)
print(max_val)
print(min_val)
