import heapq
import sys
input=sys.stdin.readline
n,m,c=map(int, input().split())
graph=[[] for _ in range(n+1)]
INF=int(1e9)
distance=[INF]*(n+1)
for _ in range(m):
    a,b,d= map(int, input().split())
    graph[a].append((b,d))
def dijsktra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist, now= heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost= dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
dijsktra(c)
count_city=0
total_time=0
for i in distance:
    if i!=INF:
        count_city+=1
        if total_time<i:
            total_time=i
print(count_city-1, total_time)
