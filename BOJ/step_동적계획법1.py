# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:15:29 2020

@author: ChangYeol
"""

# 피보나치 수 2
N = int(input())
F_0, F_1 = 0, 1
for i in range(N):
    F_0, F_1 = F_1, F_0+F_1
print(F_0)


# 피보나치 함수
def count_fibonacci(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n <= 1:
        return
 
    for i in range(2, n+1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))