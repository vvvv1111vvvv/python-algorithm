#위상정렬
from collections import deque
import copy
v=int(input())
#진입차수
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]
time=[0]*(v+1)
for i in range(1,v+1):
    temp= list(map(int, input().split()))
    time[i]=temp[0]
    for x in temp[1:-1]:
        graph[x].append(i)
        indegree[i]+=1
def topology_sort():
    q=deque()
    result=copy.deepcopy(time)

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            result[i]=max(result[i],result[now]+time[i])
            if indegree[i]==0:
                q.append(i)
    for i in range(1,v+1):
        print(result[i])
topology_sort()
