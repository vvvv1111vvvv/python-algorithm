s=str(input())
result=0
for x in s:
    if result<=1 or int(x)<=1:
        result+=int(x)
        continue
    result*=int(x)
print(result)
# 0왼쪽부호는 더하기단 첫번째이면, 오른쪽 부호 더하기
# 1은 더하기
    