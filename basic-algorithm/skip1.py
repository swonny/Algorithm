# 특정 조건일 때 반복문을 건너뛰도록

n = int(input('n 입력: '))

for i in range(n):
    if i % 3 == 0: continue
    print(f'{i}', end=' ')

print()
