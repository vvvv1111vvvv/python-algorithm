input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

count=0
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result=[]
for step in steps:
    nrow=row+step[0]
    ncolumn=column+step[1]
    if nrow<1 or nrow>8 or ncolumn<1 or ncolumn>8:
        continue
    count+=1
    ncolumn=chr(ncolumn+int(ord('a')-1))
    result.append(ncolumn+str(nrow))
print(count)
print(result)