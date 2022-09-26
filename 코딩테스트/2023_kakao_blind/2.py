users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

# 할인율 별로 각 이모티콘 별 할인율 저장
discounted = {i : [] for i in range(1, 5)}
for emo in emoticons:
    for i in range(4):
        discounted[i+1].append(emo - emo * 0.1 * (i + 1))


    
print(discounted)