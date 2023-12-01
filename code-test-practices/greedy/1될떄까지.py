n,k=map(int, input().split(" "))
count=0
while True:
	if(n<k):
		break
	elif(n%k==0):
		n=int(n/k)
		count+=1
	else:
		n-=1
		count+=1
print(count+(n-1))