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
    
    

# 통계학
import sys 
from collections import Counter

#main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))
    
def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # nums의 개수는 홀수
    
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))


# 소트인사이드
nums = input()
nums = [int(n)  for n in nums]

ordered_nums = sorted(nums, reverse=True)

for n in ordered_nums : 
    print(n, end="")
    

# 좌표 정렬하기
N = int(input())
arr = list()
for _ in range(N):
    arr.append(tuple(map(int,input().split(' '))))

arr.sort(key = lambda x : (x[0],x[1]))
for x,y in arr:
    print(x,y)


# 좌표 정렬하기 2

N = int(input())

arr = list()
for _ in range(N):
    arr.append(tuple(map(int,input().split(' '))))

arr.sort(key = lambda x : (x[1],x[0]))

for x,y in arr:
    print(x,y)


# 단어 정렬
    # first
N = int(input())
arr = set()
for i in range(N):
    word = input()
    _len = len(word)
    arr.add((word,_len))

list(arr).sort(key = lambda x : (x[1],x[0]))
for i in arr:
    print(i[0])

    # second
N = int(input())
arr = dict()
for i in range(N):
    word = input()
    _len = len(word)
    
    if _len in arr.keys():
        arr[_len].append(word)
    else :
        arr[_len] = [word]

res = list()
for i in arr.values():
    res.append(sorted(i))
    
for i in [element for row in res for element in row]:
    print(i)

    # third
    
import operator
N = int(input())
arr = dict()
for i in range(N):
    word = input()
    _len = len(word)
    
    if _len in arr.keys():
        arr[_len].append(word)
    else :
        arr[_len] = [word]

res = sorted(arr.items(), key = operator.itemgetter(0))
for i in res:
    for j in set(sorted(i[1])):
        print(j)

    