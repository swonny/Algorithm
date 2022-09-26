from sys import stdin

input = stdin.readline
n = int(input())
score = [list(map(int, input().strip().split())) for i in range(n)]
for i in range (len(score)):
    flag = False
    if score[i][0] == (score[i][1] + score[i][2]):
        flag = True
    score[i] = ((score[i][0] * (score[i][1] + score[i][2])) * 2) if flag else (score[i][0] * (score[i][1] + score[i][2]))

print(max(score))