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


# 단어의 개수
sentence = input().strip()
if sentence == '' :
    print(0)
else :
    print(sentence.count(' ') + 1)


# 상수
before = input()
after = ''
for i in range(len(before)-1,-1,-1):
    after += before[i]

after = list(map(int,after.split(' ')))
print(max(after))


# 다이얼
def to_dial(x):
    if x == 'A' or x == 'B' or x == 'C':
        return 3
    elif x == 'D' or x == 'E' or x == 'F':
        return 4
    elif x == 'G' or x == 'H' or x == 'I':
        return 5
    elif x == 'J' or x == 'K' or x == 'L':
        return 6
    elif x == 'M' or x == 'N' or x == 'O':
        return 7
    elif x == 'P' or x == 'Q' or x == 'R' or x =='S':
        return 8
    elif x == 'T' or x == 'U' or x== 'V':
        return 9
    elif x == 'W' or x == 'X' or x == 'Y' or x == 'Z':
        return 10
    else :
        pass
    
alpha = input()
sec = 0
for i in alpha:
    sec += to_dial(i)
print(sec)


    #
alpha = input().lower()
dial = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
sec = 0
for i in range(len(alpha)):
    for d in dial:
        if alpha[i] in d:
            sec += dial.index(d) + 3
print(sec)


# 크로아티아 알파벳
alpha = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for probe in croatia:
    alpha = alpha.replace(probe, '*')

print(len(alpha))


# 그룹 단어 체커
case = int(input())
res = 0
for i in range(case):
    word = input()
    if list(word) == sorted(word, key=word.find):
        res += 1
print(res)
