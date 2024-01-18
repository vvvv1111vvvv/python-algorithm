from collections import deque
def bfs(now_loc,now_dist, case):
    gloabl count
    if now_loc==case and now_dist==-1:
        return count
    while 0<=now_loc<case:
        count+=1
        dfs(now_loc+now_dist-1,now_dist-1, case)
        count-=1
        count+=1
        dfs(now_loc+now_dist,now_dist, case)
        count-=1
        dfs(now_loc+now_dist+1,now_dist+1, case)
t= int(input())
cases=[]
result=[]
for _ in range(t):
    a,b=map(int, input().split())
    cases.append(b-a)
for case in cases:
    count=0
    result.append(dfs(0,1,case))
    
        
    