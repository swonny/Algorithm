terms = ['A 6', "b 3"]

terms = {t.split(' ')[0] : t.split(' ')[1] for t in terms}
print(terms)

t = "2019.01.01 D"
a, b, c = map(int, t[:-1].split('.'))
print(a, b, c)