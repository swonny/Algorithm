# 실전 문제 3 [게임 개발]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n) ]

dx = [0, 1, 0, -1] # 북, 동, 남, 서
dy = [1, 0, -1, 0] # 북, 동, 남, 서
left_d = [3, 0, 1, 2] # 0, 1, 2, 3 에 대한 왼쪽 방향
back_d = [2, 3, 0, 1] # 0, 1, 2, 3 에 대한 뒤쪽 방향

count = 0
while True:
    if maps[x][y] == 0:
        maps[x][y] = 2 # 방문 표시
        count += 1
    i = 0
    while i < 4:
        d = left_d[d] # 왼쪽 방향으로 틀기
        nx = x + (dx[d])
        ny = y + (dy[d])
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0: # 방문 가능한 지역인 경우
            x = nx
            y = ny
            break
        i += 1
        print(x, y, d)
    if i >= 4:
        b = back_d[d]
        bx = x + dx[b]
        by = y + dy[b]
        if maps[bx][by] == 1:
            break
        else: # 바다가 아니면 위치 옮긴 뒤 continue
            x = bx
            y = by

print(count)