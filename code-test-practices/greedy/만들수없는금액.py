n=int(input())
moneys=list(map(int, input().split()))
moneys.sort()
target=1
result=0
for money in moneys:
    if money>target:
        result=target
        break
    target+=money
print(result)