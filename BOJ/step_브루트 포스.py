# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:18:07 2020

@author: ChangYeol
"""

# 블랙잭
N, M = map(int,input().split(' '))
card = list(map(int,input().split(' ')))
res = set()
for i in range(N-1):
    
    pick = card[i:i+2]
    other = [x for x in card if x not in pick]
    
    for j in other:
        
        if M >= sum(pick,j) :
        
            res.add(sum(pick,j))

print(max(res))

# 반례
# 3 10
# 3 1 3 1 4
# 연속된 카드뿐만 아니라 모든 경우의 수를 고려할 것

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
res = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            s = card[i] + card[j] + card[k]
            if s > M:
                break
            else:
                res = max(res, s)
print(res)

# library 이용
import itertools
N, M = map(int, input().split())
card = list(map(int, input().split()))
pick = itertools.combinations(card, 3)

res = 0
for i in pick:
    if sum(i) <= M:
        if res < sum(i):
            res = sum(i)
print(res)



# 분해합
# 처음 작성한 코드 (실패)            
def constructor(a):
    scope = len(a) * 9
    for probe in range( int(a) - scope , int(a) + scope + 1 ):
        s = 0
        for element in str(probe):
            s += int(element)
            if probe + s == int(a):
                return probe
    return 0
constructor()

# 수정한 코드 
def constructor(N):
    
    minimum = N - len(str(N)) * 9
    minimum = 1 if minimum < 1 else minimum
    
    for i in range(minimum, N):
        
        Sum = i
        Sum += sum(map(int,str(i)))  # 이 부분으로 2중 for문 안돌려도 된다.
        
        if Sum == N:
            print(i)
            return
        
    print(0)
    
constructor(int(input()))


# 덩치
# 자기보다 크고 무거운(둘 다 큰) 사람이 몇 명인지 쟤서 자기 등수만 정하면 된다. 
# n명을 n-1번씩 전수 비교해보면 된다.

N = int(input())
st_arr = list()

for _ in range(N):
    weight, height = map(int,input().split(' '))
    st_arr.append((weight,height))

for i in st_arr:
    rank = 1
    for j in st_arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')
    


# 체스판 다시 칠하기
# 경우의 수가 두가지
# W로 시작하는지 B로 시작하는지. 먼저 시작하는 것들이 좌표가 모두 짝수 일때 나온다.

# 두개의 함수를 생성한다. 
# 첫번째는 뒤에서 생성할 Whitboard 와 BlackBoard에서 각 좌표를 바꿔가며 비교하며
# 틀린 값이 있을 경우 count 값이 1씩 증가하도록 만든다.
# 두번 째 함수는 입력값으로 주어진 사격형 Board와 White / Black Board를 선언해주고
# 각각 모든 경우의 8 * 8 체스판의 경우를 1번 함수에 넣어 준다
# 이때 result값은 반복문이 진행되면서 가장 최소 값이 overwrite되도록 한다.
# 최초 64 는 8*8 배열에서 모두다 바뀌어야할 때의 숫자다. 즉 최대값을 우선 넣어두고
# overwrite 되도록 하였다.
    


def check_board(SQUARE, probe, move_x, move_y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if SQUARE[move_x+i][move_y+j] != probe[i][j]:
                cnt += 1
    return cnt


def check_bw():
    
    N, M = map(int,input().split())
    square = [list(input()) for _ in range(N)]
    
    WhiteBoard = [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]

    BlackBoard = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]
    
    result = 64
    
    for i in range(N-7):
        for j in range(M-7):
            W = check_board(square, WhiteBoard, i, j)
            B = check_board(square, BlackBoard, i, j)
            
            result = min(result,W,B)
    
    print(result)
check_bw()


# 영화감독 숌

# 문제 이해를 잘못함.
# 최대 10,000까지만 시리즈를 만들면 되는 줄 알았는데 그게 아니라
# 입력값이 최대 10,000
N = int(input())

arr = list()
for i in range():
    if str(i).count('666'):
        arr.append(i)
        
print(arr[N-1])


# 다시 만든 풀이
# for문이 돌면서 인풋값 길이 만큼 생성됬을 때 while이 멈추도록 함
N = int(input())
i = 0
arr = list()
while True:
    i += 1
    
    if str(i).count('666'):
        arr.append(i)
        
    if len(arr) == N:
        break
print(arr[-1])
