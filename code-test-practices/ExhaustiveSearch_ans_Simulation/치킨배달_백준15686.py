from itertools import combinations, permutations
import math
def chicken_length(house, chicken):
    sum=0
    for home in house:
        each_chicken_length=98
        for shop in chicken:
            each_chicken_length=min(each_chicken_length, abs(home[0]-shop[0])+abs(home[1]-shop[1]))
        sum+=each_chicken_length
    return sum
n,m= map(int, input().split())
d=[[0]*(n+1)]
for _ in range(n):
    d.append([0]+list(map(int, input().split())))
house=[]
chicken=[]
for r in range(1,n+1):
    for c in range(1, n+1):
        if d[r][c]==2:
            chicken.append([r,c])
        elif d[r][c]==1:
            house.append([r,c])
min_city_length=int(1e9)
comb=list(combinations(chicken,m))
for val in comb:
    min_city_length=min(min_city_length, chicken_length(house, val))
print(min_city_length)
