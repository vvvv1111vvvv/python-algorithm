#맞는지는 모르겠음
n=int(input())
array=list(map(int, input().split()))
group=[]
t=0
array.sort()
i=0
while i<len(array):
    temp=[]
    if i+array[i]+t-1>=len(array):
            break
    for j in range(i,i+array[i]+t):
        temp.append(array[j])
    if max(temp)== len(temp):
        group.append(temp)
        i=i+array[i]+t
        t=0
    else:
        t=t+1
print(len(group))