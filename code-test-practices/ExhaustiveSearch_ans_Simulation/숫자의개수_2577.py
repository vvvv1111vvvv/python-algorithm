val=1
for _ in range(3):
    val*=int(input())
val=str(val)
for i in range(10):
    each_count=0
    for digit in range(len(val)):
        if i==int(val[digit]):
            each_count+=1
    print(each_count)