n= int(input())
temp=[]
for _ in range(n):
    temp.append(int(input()))
#temp.sort()
#temp.reverse()
temp=sorted(temp,reverse=True)
for data in temp:
    print(data, end=" ")