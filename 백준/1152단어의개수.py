from sys import stdin

n = int(input())
users = [stdin.readline().split()+[i] for i in range(n)]
users = [(int(age), name, i) for i, (age, name) in enumerate(users)]
users = sorted(users, key=lambda x: (x[0], x[2]))

for i in range(n):
    print(f'{users[i][0]} {users[i][1]}')