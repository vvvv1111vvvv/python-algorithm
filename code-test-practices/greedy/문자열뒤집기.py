data= input()
count_0=0
count_1=0
series_0=0
series_1=0
for i in range(len(data)):
    if int(data[i])==0:
        series_0+=1
        if series_1!=0:
            series_1=0
            count_1+=1
    else:
        series_1+=1
        if series_0!=0:
            series_0=0
            count_0+=1
if series_0!=0:
    count_0+=1
else:
    count_1+=1
if(count_0>=count_1):
    print(count_1)
else: 
    print(count_0)
