#https://school.programmers.co.kr/learn/courses/30/lessons/60060
#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the tasks function below.
from collections import deque
def search(n,a,b, parent, pass_ele):
    count=1
    for i in range(len(a)):
        if b[i]==parent and a[i]!=pass_ele:
            q=deque([i])
            while q:
                new_parent_idx=q.popleft()
                count+=1
                for j in range(len(a)):
                    if b[j]==a[new_parent_idx]:
                        if a[j] == b[new_parent_idx]:
                            count+=min(search(n,a,b,a[j],b[j]), search(n,a,b,b[j],a[j]))
                        else:
                            q.append(j)
    return count
    
def tasks(n, a, b):
    result=n
    checked=[False]*(100001)
    for i in range(len(a)):
        if checked[a[i]]==False and (b[i] in a) and a[i] == b[a.index(b[i])]:
            result-=min(search(n,a,b,a[i],b[i]), search(n,a,b,b[i],a[i]))
            checked[a[i]]=True
            checked[b[i]]=True
    return result

