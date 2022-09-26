from sys import stdin

input = stdin.readline
n = int(input())
stk = []
score = 0
for i in range(n):
    tmp = input().rstrip()
    if tmp == '0':
        if len(stk) > 0:
            tmp = stk.pop()
        else:
            continue
    else:
        tmp = list(map(int, tmp.split()))
    tmp[2] = tmp[2] - 1
    if tmp[2]:
        stk.append(tmp)
    else:
        score += tmp[1]

print(score)

# 점수 입력
# """

# """
        