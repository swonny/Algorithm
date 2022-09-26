id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3


count = [0] * len(id_list)
id_dict = {i : set() for i in id_list}
for r in report:
    a, b = r.split()
    id_dict[b].add(a)

for d in id_dict:
    if len(id_dict[d]) >= k:
        for i in id_dict[d]:
            count[id_list.index(i)] += 1

print(count, id_dict)