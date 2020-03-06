# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:15:29 2020

@author: ChangYeol
"""

# 피보나치 수 2
N = int(input())
F_0, F_1 = 0, 1
for i in range(N):
    F_0, F_1 = F_1, F_0+F_1
print(F_0)


# 피보나치 함수
def count_fibonacci(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n <= 1:
        return
 
    for i in range(2, n+1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))
    
    


# 01타일
def tile001(n):
    answer = 0
    temp_1 = 1
    temp_2 = 2
    for i in range(1, n+1):
        if i == 1:
            answer = temp_1
        elif i == 2:
            answer = temp_2
        else:
            answer = temp_1 + temp_2
            temp_1 = temp_2 % 15746
            temp_2 = answer % 15746
    
    print(answer % 15746)
        
tile001(int(input()))


# 파도반 수열

t = int(input())
dp = [0 for _ in range(101)]

def wave():
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2
    dp[6] = 3
    for i in range(7, 101):
        dp[i] = dp[i-1] + dp[i-5]
    return

for _ in range(t):
    n = int(input())
    wave()
    print(dp[n])
    
    
    
# RGB거리
def solve():
    for i in range(3):
        d[1][i] = p[1][i]
    for i in range(2, n+1):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + p[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + p[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + p[i][2]
    print(min(d[n]))

n = int(input())
d = [[0]*3 for _ in range(n+1)]
p = [[0]*3]+[list(map(int, input().split())) for _ in range(n)]
solve()


# 정수 삼각형
triangle = int(input())
triangle_matrix = []
max_matrix = [[] for _ in range(triangle)]

for _ in range(triangle):
    triangle_matrix.append(list(map(int, input().split())))

#역순으로 하위 항목을 모두 더한 최댓값을 저장
for i in range(triangle - 1, -1, -1):
    for j in range(len(triangle_matrix[i])):
        if i == triangle - 1:
            max_matrix[i].append(triangle_matrix[i][j])
        else:
            max_matrix[i].append(triangle_matrix[i][j] + max(max_matrix[i+1][j], max_matrix[i+1][j+1]))

print(max_matrix[0][0])


# 계단 오르기
# https://daimhada.tistory.com/181
# https://this-programmer.com/entry/%EB%B0%B1%EC%A4%802579%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0
stairs = int(input())
stair_list = [0]
result = [[0, 0] for _ in range(stairs + 1)]

for _ in range(stairs):
    stair_list.append(int(input()))

for i in range(1, stairs + 1):
    if i == 1:
        result[1][0] = stair_list[1]
    elif i == 2:
        result[2][0] = stair_list[1] + stair_list[2]
        result[2][1] = stair_list[2]
    else:
        result[i][0] = max(result[i-3]) + stair_list[i-1] + stair_list[i]
        result[i][1] = max(result[i-2]) + stair_list[i]

print(max(result[stairs]))



    # 참고 
stair_count = int(input())
stair_scores_list = list()
stair_scores_list.append(0)

for i in range(stair_count):
    stair_scores_list.append(int(input()))

sum_of_score = list()
sum_of_score.append(0)
sum_of_score.append(stair_scores_list[1])
sum_of_score.append(stair_scores_list[1] + stair_scores_list[2])
sum_of_score.append(max(stair_scores_list[3] + stair_scores_list[1], stair_scores_list[3] + stair_scores_list[2]))

for i in range(4, stair_count + 1):
    sum_of_score.append(max(stair_scores_list[i] + sum_of_score[i - 2],
                            stair_scores_list[i] + stair_scores_list[i - 1] + sum_of_score[i - 3]))

print(sum_of_score[-1])



# 1로 만들기
def min(x, y):
    return x if x <= y else y
 
x = int(input())
 
minimum_count = [ 0 for _ in range(x+1)]
 
index = 0
while(True):
    if index > x:
        break
 
    if index <= 1:
        minimum_count[index] = 0
    else:
        temp_min = x + 1
        if index % 3 == 0:
            temp_index = int(index/3)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        if index % 2 == 0:
            temp_index = int(index/2)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        temp_min = min(temp_min, minimum_count[index-1])
        minimum_count[index] = int(temp_min + 1)
    index = index + 1
 
print(minimum_count[x])


# 쉬운 계단 수
stair_numbers = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1:
            stair_numbers[i][j] = 1
        else:
            if 1 <= j <= 8:
                stair_numbers[i][j] = stair_numbers[i-1][j-1] + stair_numbers[i-1][j+1]
            elif j == 0:
                stair_numbers[i][j] = stair_numbers[i-1][j+1]
            elif j == 9:
                stair_numbers[i][j] = stair_numbers[i-1][j-11]
                
N = int(input())             
print(sum(stair_numbers[N][1:10]) % 1000000000)


# 포도주 시식
wine = int(input())
wine_capa = [0]
result = [0 for _ in range(wine + 1)]

for _ in range(wine):
    wine_capa.append(int(input()))

for i in range(1, wine + 1):
    if i == 1:
        result[1] = wine_capa[1]
    elif i == 2:
        result[2] = wine_capa[1] + wine_capa[2]
    else:
        result[i] = max(result[i-3] + wine_capa[i-1] + wine_capa[i], result[i-2] + wine_capa[i], result[i-1])  

print(result[i])