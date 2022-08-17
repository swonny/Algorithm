from sys import stdin
from collections import deque

t = int(stdin.readline().rstrip())
for _ in range(t):
    p = stdin.readline().rstrip()
    n = int(stdin.readline().rstrip())
    arr = deque(list(stdin.readline().rstrip()[1:-1].split(',')))
    if arr:
        arr = deque(list(map(int, arr)))

    flag = 0
    for comm in p:
        if comm == 'R':
            flag = 0 if flag else 1
        else:
            try:
                if flag:
                    arr.pop()
                else:
                    arr.popleft()
            except IndexError:
                arr = 'error'
                break
    
    if arr == 'error':
        print(arr)
    else:
        if flag:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')