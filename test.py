from sys import stdin

n = int(input())
stk = []
ptr = 0 # 수열 ptr
top = 0 # 스택 데이터 개수
result = []

numarr = list([input() for _ in range(n)])
for num in range(1, n+1):
    stk.append(num) # push
    top += 1
    result.append('+')

    while top > 0 and stk[top - 1] == int(numarr[ptr]):
        stk.pop()
        top -= 1
        result.append('-')
        ptr += 1

if(top > 0):
    stk.reverse()
    stkStr = ''.join(map(str, stk))
    numarrStr = ''.join(map(str, numarr[ptr:]))
    if stkStr == numarrStr:
        result.append(stkStr.split())
    else:
        print('NO')
        result= []

for n in result:
    print(n)


#     8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1