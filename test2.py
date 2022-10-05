from sys import stdin

n = int(input())
meetings = [tuple(map(int, stdin.readline().strip().split())) for _ in range(n)]
meetings = sorted(meetings)

s, e, t = meetings[0][0], meetings[0][1], meetings[0][1] - meetings[0][0]
count = 1
for meeting in meetings[1:]:
    if meeting[1] - meeting[0] < t and meeting[1] <= e:
        s = meeting[0]
        e = meeting[1]
        t = meeting[1] - meeting[0]
    elif meeting[0] >= e:
        s = meeting[0]
        e = meeting[1]
        t = meeting[1] - meeting[0]
        count += 1
    print(meeting, count)

print(count)