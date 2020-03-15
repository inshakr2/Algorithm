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