# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:08:34 2020

@author: ChangYeol
"""
# N과 M 1
# https://codedrive.tistory.com/194

N,M = map(int,input().split())

num_list = [i for i in range(1,N+1)]
check_list = [False]*N

arr = []

# 주어진 개수가 채워지면 출력된다.
def dfs(cnt):
    # 갯수가 찬 경우 arr을 출력하고 끝난다.
    # 아래 for에서 마지막 순환 때 cnt+1이 되어 for반복수만큼 dfs가 다시 호출된다.
    # 그럼 그 반복수만큼 이 부분이 실행되게 되는 것이다.
    if cnt==M:
        print(*arr)
        return

    for i in range(N):
        # 이미 나온 값은 거른다.
        if check_list[i]:
            continue

        # 나올 수 리스트들에 대한 for이기 때문에 i는 첫번째 노드가 된다.
        # 그래서 등장한 것으로 추가하고 num_list를 추가한다.
        check_list[i] = True
        arr.append(num_list[i])

        # 다음번째로 골라질 숫자
        dfs(cnt+1)

        # 리스트를 계속 사용하기 위해 위의 재귀가 호출되고 나면 한 자리를 pop시킨다.
        # pop시켰으므로 false로 만들어준다.
        arr.pop()
        check_list[i] = False

# 호출할 때의 인자는 재귀함수에서 현재 몇 자리를 찾았는지 확인할 때 사용한다.
dfs(0)


# 1
def sequence(stack,numbers,M):
    if len(stack)==M:
        print(*stack)
        return
    else:
        for number in numbers:
            if not number in stack:
                stack.append(number)
                sequence(stack,numbers,M)
                stack.pop()
 
a,b=map(int,input().split())
numbers=list(range(1,a+1))
stack=[]
for number in numbers:
    if not number in stack:
        stack.append(number)
        sequence(stack,numbers,b)
        stack.pop()
        
        

# 2
        
def go(N, M, count, line, excludes):
	global arr
	if M == count:
		print(line)
	else:
		if count == 0:
			for i in range(N):
				if i not in excludes:
					go(N, M, count+1, str(arr[i]), excludes + (i, ))
		else:
			for i in range(N):
				if i not in excludes:
					go(N, M, count+1, line + " " + str(arr[i]), excludes + (i, ))

N, M = map(int, input().split(" "))

arr = list(range(1, N+1))

go(N, M, 0, "", ())


# 3
def npr(n, k, N):
    if n == k:
        print(' '.join(map(str, p)))
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1, k, N)
                used[i] = 0

N, M = map(int, input().split())
used = [0] * N
p = [0] * M
npr(0, M, N)

# N과 M 2
# https://wlstyql.tistory.com/58?category=852442
N, M = map(int, input().split())
visited = [False] * N
out, out_all = [], []

def solve(depth, N, M):
    if depth == M:
        out_str = ' '.join(map(str, sorted(out)))
        if out_str not in out_all:
            out_all.append(out_str)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()
solve(0, N, M)

for i in out_all:
    print(i)


# N과 M 3
N, M = map(int, input().split())
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)
    

# N과 M 4
def f(n,m,k,l):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(arr[i] >= l):
                visited[i] = 1
                l = arr[i]
                res[n] = arr[i]
                f(n+1,m,k,l)
                visited[i] = 0

n, m = map(int, input().split())
arr = range(1,n+1)
visited = [0 for i in range(n)]
res = [0] * m
f(0,n,m,0)


# N-Queens

# 1
# https://geonlee.tistory.com/40
# https://codepractice.tistory.com/82
def nqueen(sol, n):
    
    global count
    
    if len(sol) == n: # 정답 배열(sol)의 길이가 n과 같아지면, count 증가
        count += 1
        return 0
    
    candidate = list(range(n)) # 0부터 n-1까지를 후보 배열로 만든다.
    
    for i in range(len(sol)):
        if sol[i] in candidate: # 같은 열에 있는 지 확인
            candidate.remove(sol[i]) # 같은 열에 있다면 후보에서 제외
            
        distance = len(sol) - i
        
        if sol[i] + distance in candidate: # 같은 대각성 상(+)에 있는 지 확인
            candidate.remove(sol[i] + distance) # 같은 대각선 상에 있다면 후보에서 제외
            
        if sol[i] - distance in candidate: # 같은 대각선 상(-)에 있는 지 확인
            candidate.remove(sol[i] - distance) # 같은 대각선 상에 있다면 후보에서 제외
            
    if candidate != []:
        for i in candidate:
            sol.append(i) # 후보의 요소를 정답 배열의 i+1로 추가
            nqueen(sol, n) # 재귀적으로 다음 행도 확인
            sol.pop()
    else:
        return 0
count = 0
num = int(input())
for i in range(num): # 첫 행의 경우의 수
    nqueen([i], num)
print(count)

count = 0
nqueen([8],8)
print(count)

# 2
def isPromising(k, col): # k번째 row에서 Queen이 col번째 column에 놓을 수 있는지 (k-1번째 row까지) 검사하는 함수
    for row in range(1, k): # 1번째 row부터 k-1번째 row까지 검사
        if col == x[row] or abs(col - x[row]) == abs(k - row): # row번째 Queen과 놓으려는 Queen이 같은 직선이나 대각선 상에 있는 경우
            return False # 해당 위치에는 Queen을 놓을 수 없음
    return True # 위의 조건에 해당되지 않으면, Queen을 해당 위치에 놓을 수 있는 것임
 
def nQueens(k): # 문제 해결을 위한 함수
    global count # count변수는 전역 변수로 이용함
    for col in range(1, N + 1): # 1번째 column부터 N번째 column까지 일일히 검사
        if isPromising(k, col) == True: # k번째 row에서 col번째 column에 Queen을 놓을 수 있는 경우
            x[k] = col # k번째 row에서 Queen의 위치는 col번째 column임
            if k < N:
                nQueens(k + 1) # 다음 row검사(nQueens함수 다시 호출)
            else:
                count += 1 # 가능한 방법의 수 증가
 
count = 0 # 구하고자 하는 방법의 수
N = int(input()) # 체스판의 크기(N x N에서 N)
x = [0]*(n + 1) # x[1]부터 x[N]까지 사용을 하기 위해 배열 동적 할당
nQueens(1) # 1번째 row부터 각 row와 column별로 검사하기 위해 nQueen(1)을 호출
print(count)




# 스도쿠
sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)



# 연산자 끼워넣기
# https://claude-u.tistory.com/371
from itertools import permutations #순열 함수

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

#각각의 연산자를 모두 입력
operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * division

#중복되지 않게 연산자 셋을 종류별로 만들어줌
operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
operation_set = list(set(operation_set)) #중복 제거

#+, -, *, //가 나올 경우를 나누어준다
max_answer = -1000000001
min_answer = 1000000001
for case in operation_set:
    answer = A[0] #첫 값 대입
    
    for i in range(N-1):
        if case[i] == 1:
            answer += A[i+1]
        elif case[i] == 2:
            answer -= A[i+1]
        elif case[i] == 3:
            answer *= A[i+1]
        elif case[i] == 4: #나눗셈 정의를 문제에 따라줌
            if answer < 0: 
                answer = -(-answer // A[i+1])
            else:
                answer //= A[i+1]
                
    #최댓값 최솟값일 경우
    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer
    
print(max_answer)
print(min_answer)


# 스타트와 링크

import itertools
import sys
n=int(sys.stdin.readline().strip())
temp=list(range(n))
synergy=[]
for i in range(n):
    synergy.append(list(map(int,sys.stdin.readline().strip().split())))
p = list(itertools.combinations(temp,n//2))
answer=[]
for team in p:
    start = list(team)
    link = list(set(temp)-set(team))
    Synergy_start=0
    Synergy_link=0
    for i in start:
        for j in start:
            Synergy_start+=synergy[i][j]
    for i in link:
        for j in link:
            Synergy_link+=synergy[i][j]
    ans=abs(Synergy_link-Synergy_start)
    answer.append(ans)
print(min(answer))