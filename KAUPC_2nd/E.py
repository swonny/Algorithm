# 비행기

# 출력 : 부품이 언제 출발했고 언제 도착했는지

# 처음 트럭 0번 위치
# 이동시간 T
# 부품이 준비되는 시간이 동일한 경우 트럭이 현재 위치한 곳부터 싣는다
# 운송이 준비되는 시간

# 트럭의 위치 변수 : 0 / 1 (초기값 0)
# 0일 때 준비시간이 0이면 현재시간 + 10에 도착, 트럭 1로 업데이트
# 준비시간이 현재시간보다 작거나 같으면 바로 출발 가능

from sys import stdin
from collections import deque

input = stdin.readline

N, M, T = map(int, input().strip().split())
l = [list(map(int, input().strip().split())) for i in range(N)]

cur = 0
w = 100
truck = 0
stk = deque()
i = 0
print(N)
while True:
    if i >= N:
        if not stk:
            break
        else:
            i = stk.popleft()
    print(f'cur :{cur} truck: {truck} w : {w}')
    if truck == l[i][0]:
        if l[i][2] > cur:
            if stk and l[stk[0]][2] < l[i][2]:
                i = stk.popleft()
            cur += (l[i][2] - cur)
        if l[i][2] <= cur: # weight 조건?
            if truck != l[i][0]:
                cur += 10
                truck = 0 if truck else 1
            l[i] = [cur, cur + 10]
            cur += 10
            truck = 0 if truck else 1
            w -= l[i][1]
    else:
        if l[i][2] <= cur:
            # tmp = w - l[i][1]# 남은 자리에 들어갈 수 있는 무게
            # print(f'tmp : {tmp} w : {w}  l[i][1]: {l[i][1]}')
            tmp = l[i][1]
            l[i][1] -= w
            w = 100
        stk.append(i)

    if i < N:
        i += 1
    else:
        if stk:
            i = stk.popleft()
        else:
            break
    print(f'i : {i}')
    print(l)

    
# for i in l:
#     print(f'{i[0]} {i[1]}')

print(l)