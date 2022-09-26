# i 번째 날의 최댓값을 알아야함
# i - 1번째 날에 선택한 디저트 번호를 알아야함
# i - 1번째 날에 선택한 디저트 번호와 i 번째 최댓값 디저트 번호가 같다면 최댓값 //= 2로 update하여 최댓값 찾기.

# 딕셔너리로 1일 ~ n번째 날 생성
# 각 날짜에 해당하는 리스트 생성
from sys import stdin

n, m = map(int, input().split())
dessert = {n : list() for n in range(n)}
for i in range(m):
    tmp = list(map(int, stdin.readline().rstrip().split()))
    for i in range(n):
        dtmp = dessert[i]
        dtmp = dtmp.append(tmp[i])
        # dessert[i] = dessert[i].append(tmp[i])
        # print(dtmp)

prev = 0 # i - 1번째 최대 개수의 디저트 번호
res = []
for i in range(n):
    tmpMax = dessert[i].index(max(dessert[i]))
    if prev == tmpMax:
        # p1 = max(dessert[i-1])
        # max()
        dessert[i][tmpMax] //= 2
    prev = dessert[i].index(max(dessert[i]))
    res.append(max(dessert[i]))

print(sum(res))

# prev와 같으면 이전 두번째로 큰 수 + 현재 큰수, 이전 큰 수 + 현재 큰수//2 중 max
