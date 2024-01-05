data=input()
result=[]
value=0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)
result.sort()
if value!=0:
    result.append(str(value))
print(''.join(result))

'''import re
s=input()
sum=0
data=re.findall('[0-9]', s)
for val in data:
    sum+=int(val)
    data=[]
data=re.findall('[A-Z]', s)
data.sort()
for i in data:
    print(i, end="")
print(sum)
'''


