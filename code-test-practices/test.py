from collections import deque
def bfs(now_loc,now_dist, case):
    q=deque()
    q.append((now_loc,now_dist,case))
    count=0
    while q:    
        sz=len(q)
        for _ in range(sz):
            if now_loc==case and now_dist==1:
                result.append(count+1)
                break
            q.append((now_loc+now_dist-1,now_dist-1, case))
            q.append((now_loc+now_dist,now_dist, case))
            q.append((now_loc+now_dist+1,now_dist+1, case))
        count+=1
             
t= int(input())
cases=[]
result=[]
for _ in range(t):
    a,b=map(int, input().split())
    cases.append(b-a)
for case in cases:
    result.append(bfs(0,1,case))
for i in range(len(result)):
    print(result[i])
        
    