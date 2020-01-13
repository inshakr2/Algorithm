# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:42:25 2020

@author: ChangYeol
"""

# 손익분기점
 
A, B, C = map(int,input().split(' '))
if B >= C :
    print(-1)
else :
    print((A // (C-B)) +1)

A + (B * n) - (C * n) > 0
A + (B - C) * n > 0
n > A / (C-B)

#data = list(map(int,input().split(' ')))
#A = data.pop(0)
#B = data.pop(0)
#C = data.pop(0)
#
#if B >= C :
#    print(-1)
#else :
#    cn = 1
#    while cn * B + A > C * cn:
#        cn += 1
#    print(cn + 1)


# 설탕 배달
kg = int(input())
cn = 0

while True:
    if (kg % 5 != 0) and (kg > 0):
        kg -= 3
        cn += 1
    else:
        break

if kg % 5 != 0:
    print(-1)
else:
    cn += int(kg / 5)
    print(cn)


# 벌집
1 7 19 37 61
 6n

6 * {n (n-1) / 2} + 1
= 3 (n * (n-1) ) + 1

x = int(input())
n = 1
while 3*(n*(n-1)) + 1 < x:
    n += 1
print(n)


# 분수찾기
1 2 3 4 ...
S = n(n+1) / 2
1 3 6 10 15 

def SUM(n):
    return int((n*(n+1)) / 2)

X = int(input())
n = 1

while SUM(n) < X :
    n+=1

if n % 2 != 0:
    rem = X - SUM(n-1)
    mom = n - rem + 1
    print('{}/{}'.format(mom, rem))
else :
    mom = X - SUM(n-1)
    rem = n - (mom-1)
    print('{}/{}'.format(mom, rem))
