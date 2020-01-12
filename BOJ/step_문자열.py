# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:23:54 2020

@author: ChangYeol
"""

# 아스키코드
print(ord(input()))


# 숫자의 합
long = int(input())
n = input()

res = 0
for i in n:
    res += int(i)
print(res)


# 알파벳 찾기
S = input()
probe = 'abcdefghijklmnopqrstuvwxyz'

for i in probe:
    print(S.find(i), end=' ')


# 문자열 반복
case = int(input())
for i in range(case):
    
    S = input().split(' ')
    R = int(S.pop(0))
    P = ''
    
    for i in S[0]:
        P += i * R
    
    print(P)


# 단어 공부
from collections import Counter
from operator import itemgetter

alpha = input().upper()
count = Counter(alpha)
count = sorted(count.items(), key=itemgetter(1), reverse = True)
if len(count) != 1 and (count[0][1] == count[1][1]):
    print('?')
else :
    print(count[0][0])
