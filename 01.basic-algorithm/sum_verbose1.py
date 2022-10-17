print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요: '))
b = int(input('정수 b를 입력하세요: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

# 여기서 만약 a가 1, b가 100이라면 else 문은 마지막 한 번에만 사용되지만 100번 반복하므로 좋은 코드가 아니다.

print(sum)