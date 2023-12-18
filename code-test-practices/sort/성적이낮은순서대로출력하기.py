def arrayfunc(data):
    return data[1]
n= int(input())
array=[]
for _ in range(n):
    temp=input().split()
    array.append((temp[0],int(temp[1])))
array.sort(key=arrayfunc)
array.reverse()
for student in array:
    print(student[0], end=" ")