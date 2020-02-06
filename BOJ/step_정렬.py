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
    
# 수 정렬하기 2
N = int(input())

arr = list()
for i in range(N):
    arr.append(int(input()))
    
# short coding
arr = [int(input()) for i in range(int(input()))]
print('\n'.join(map(str,sorted(arr))))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

for i in sorted(arr):
    print(i)
