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
    
    

# 수 정렬하기 3
import sys

case = int(input())
result = [0 for i in range(10001)]
for num in sys.stdin:
    result[int(num)] += 1

for i in range(10001):
    if result[i] > 0:
        for j in range(result[i]):
            print(i)

# short coding
# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
arr = [0] * 10000
N = int(sys.stdin.readline())
for _ in range(N):
    arr[int(sys.stdin.readline()) - 1] += 1
for i in range(10000):
    print(i + 1) for _ in range(arr[i])
