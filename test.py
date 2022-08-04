t = int(input())

for _ in range(t):
    tmp = list(map(int, input().split()))
    N, score = tmp[0], tmp[1:]
    avg = sum(score)/N
    res = [n for n in score if n > avg]
    print(format(len(res)/N*100, '.3f'), end='%\n')