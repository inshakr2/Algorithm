# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:02:16 2020

@author: ChangYeol
"""

# 수 정렬하기
N = int(input())

arr = list()
for i in range(N):
    
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)