# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:47:48 2020

@author: ChangYeol
"""


# 15596 정수 N개의 합

def solve(a):
    result = 0
    for i in a:
        result += i
    return(result)
    


# 4673 셀프 넘버
    
def d(n):
    res = 0
    for i in str(n):
        res += int(i)
        
    return res + n

res = []
for i in range(1,10000):
    res.append(d(i))
    if i not in res :
        print(i)

    
# 1065 한수

num = 0

def is_hans(n):
    n = list(map(int,list(str(n))))
    global num
    
    if n[1] - n[0] == n[2] - n[1]:
        num += 1
cycle = int(input())


for i in range(1, cycle+1):
    if i < 100 :
        num += 1
    else :
        is_hans(i)
        
print(num)
