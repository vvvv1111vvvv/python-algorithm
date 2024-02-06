n, c=map(int, input().split())
houses=[]
for _ in range(n):
    houses.append(int(input()))
houses.sort()
min_distance=1
max_distance=houses[-1]-houses[0]
while min_distance<=max_distance:
    mid_distance=(max_distance+min_distance)//2
    now_house=houses[0]
    count=1
    for house in houses:
        if house-now_house>=mid_distance:
            count+=1
            now_house=house
    if count>=c:
        result=mid_distance
        max_distance=mid_distance-1
    else:
        min_distance=mid_distance+1
print(result)