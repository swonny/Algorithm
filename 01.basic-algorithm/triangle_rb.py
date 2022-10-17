n = int(input('n을 입력하세요: '))

for i in range(n):
    for j in range(n-(i+1)):
        print(' ', end='')
    for k in range(i + 1):
        print('*', end='')
    print()