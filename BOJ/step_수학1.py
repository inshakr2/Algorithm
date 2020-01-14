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


# 달팽이는 올라가고 싶다.
    
    ## time over
A, B, V = map(int,input().split(' '))
cn = 0
height = 0
while True:
    cn += 1
    height += A
    if height >= V:
        break
    else:
        height -= B
print(cn)


### SOLUTION
V - A = H : 마지막날 전까지 올라가야할 높이
H / (A-B) 의 몫 : 마지막 전날 까지 올라가야할 날짜, 
            나머지 : 남은 높이

- 나머지가 0이면, 정확히 나누어 떨어진다는 뜻이므로 몫 + 1 (마지막 날에 하루 더 A만큼 올라가면 되므로)
- 나머지가 0이 아니라면, 이 나머지는 A-B값 보다 무조건 작다.
    따라서 나머지는 처음 우리가 최초 높이에서 A를 빼주었기 때문에 최초 높이 기준에서
    실제로 남은 높이는 A < 남은높이 < A + (A-B) 이다.
    여기서 A를 빼준다고 해도 0 < 남은 높이 < (A-B) A-B 만큼 한번 올라가야하고,
    올라가더라도 A만큼이 남아있기 때문에 A 만큼 한번더 올라가야하기 때문에
    몫 + 2 를 해준다.
    
A, B, V = map(int,input().split(' ')) 
day, remain = divmod((V - A), (A - B)) 
if remain == 0:
    print(day + 1)
else :
    print(day + 2)    



# ACM 호텔
N // H : 몇번째 W 인지? 나머지가 있으면, 몫 + 1 에 나머지 만큼 층이 올라감
                           없으면, 몫에 H만큼 층이 올라감 
                           몫은 방 번호
case = int(input())
H, W, N = map(int, input().split(' '))

room_num, rem = divmod(N, H)

if rem == 0:
    print(H,room_num)
else :
    print(rem, room_num+1)
 


if rem == 0:
    print(str(H) + '0' + str(room_num) if room_num < 10 else str(room_num) )
else :
    room_num += 1
    print(str(rem) + '0' + str(room_num) if room_num < 10 else str(room_num) )