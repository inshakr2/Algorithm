# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:06:04 2020

@author: ChangYeol
"""

# 소수 찾기
# 2 ~ n-1 의 숫자까지 나누어 지는 수가 있는지 판별 (느리다)

def Prime(n):
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    else :
        D = 0
        for i in range(2,n):
            if n % i == 0:
                D += 1
        
        if D == 0 :
            return 1
        else :
            return 0

case = int(input())
test = list(map(int,input().split(' ')))
cnt = 0
for i in test :
    cnt += Prime(i)
print(cnt)
