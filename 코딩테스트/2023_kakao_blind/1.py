
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

# today = "2008.09.21"
# terms = ["A 39"] # 15 39
# privacies = ["2000.09.21 A"]

answer = []
cY, cM, cD = map(int, today.split('.'))
y, m, d = map(int, today.split('.'))
terms = {t.split(' ')[0] : int(t.split(' ')[1]) for t in terms}
for i, priv in enumerate(privacies):
    y, m, d = map(int, priv[:-1].split('.'))
    t = priv[-1]
    if m + terms[t] > 12:
        y += terms[t] // 12
        m += terms[t] % 12
        if m > 12:
            y += 1
            m = m % 12
    else:
        m = m + terms[t]

    if d - 1 < 1:
        m -= 1
        d = 28
    else:
        d -= 1
    if y > cY:
        continue
    elif y == cY and m > cM:
        continue
    elif y == cY and m == cM and d >= cD:
        continue
    else:
        answer.append(i + 1)

print(answer)