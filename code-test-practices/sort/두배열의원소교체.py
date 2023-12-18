n,k=map(int, input().split())
array1=sorted(list(map(int, input().split())))
array2=sorted(list(map(int, input().split())), reverse=True)
for i in range(k):
    if array1[i] <array2[i]:
        array1[i], array2[i]=array2[i], array1[i]
    else:
        break
result=0
for data in array1:
    result+=data
print(result)
