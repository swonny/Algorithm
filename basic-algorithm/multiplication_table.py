# 구구단 출력

# 이중 for문을 돌려서 바깥쪽 i * j 형태로 나타내기

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end=' ')
        # print(f'{i} * {j} = {i * j:3}')
    print()