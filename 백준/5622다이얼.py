# 각 초 + 1만큼의 시간 소요
# 2부터 9까지 알파벳 존재
n = input()
cnt = 0
for e in n:
    if 'A' <= e <= 'C':
        cnt += 3
    elif 'D' <= e <= 'F':
        cnt += 4
    elif 'G' <= e <= 'I':
        cnt += 5
    elif 'J' <= e <= 'L':
        cnt += 6
    elif 'M' <= e <= 'O':
        cnt += 7
    elif 'P' <= e <= 'S':
        cnt += 8
    elif 'T' <= e <= 'V':
        cnt += 9
    else:
        cnt += 10
    
print(cnt)