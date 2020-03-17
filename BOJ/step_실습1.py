# -*- coding: utf-8 -*-


# 평균 점수 
score_list = []
for i in range(5):
    score = int(input())
    if score >= 40:
        score_list.append(score)
    else:
        score_list.append(40)
print(round(sum(score_list)/5))


# 상근날드

a = 2000
c = 2000
for i in range(3):
    b = int(input())
    a = min(a, b)
for i in range(2):
    b = int(input())
    c = min(c, b)
print(a + c - 50)


# 별찍기 13

N = int(input())

for i in range(1, N+1):
    print('*' * i)
    
for i in range(N-1, 0 , -1):
    print('*' * i)
    
    
# 별찍기 9
N = int(input())

for i in range(N-1, 0, -1):
    print(' '*(N-i-1) + ('*'*(2*i+1)))

for i in range(N):
    print(' '*(N-i-1) + ('*'*(2*i+1)))