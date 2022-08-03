# 직각이등변삼각형 출력

n = int(input('n을 입력하세요: '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    print()