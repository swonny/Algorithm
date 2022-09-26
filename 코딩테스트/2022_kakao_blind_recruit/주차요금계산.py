import math

# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [180, 5000, 10, 600]

records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
fees = [120, 0, 60, 591]

# records = ["00:00 1234 IN"]
# fees = [1, 461, 1, 10]

records_d = dict()
for r in records:
    tmp = r.split(' ')
    h, m = map(int, tmp[0].split(':'))
    tmp[0] = (h * 60) + m
    if tmp[1] not in records_d:
        records_d[tmp[1]] = []
    records_d[tmp[1]].append(tmp[0])

for r in records_d:
    tmp = 0
    for j in range(0, len(records_d[r]), 2):
        try:
            tmp += records_d[r][j + 1] - records_d[r][j]
        except IndexError:
            tmp += 1439 - records_d[r][j]
    if tmp > fees[0]:
        records_d[r] = math.ceil((tmp - fees[0]) / fees[2]) * fees[3] + fees[1]
    else :
        records_d[r] = fees[1]

records_d = sorted(records_d.items())
answer = [t[1] for t in records_d]
print(answer)