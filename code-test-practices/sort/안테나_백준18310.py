n=int(input())
house=list(map(int, input().split()))
house.sort()
if len(house)==1:
    print(house[0])
else:
    mid=(house[0]+house[-1])//2
    while True:
        if mid in house:
            print(mid)
            break
        mid=mid-1