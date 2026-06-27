"""for文との組み合わせ 解答"""

scores = [85, 92, 78, 95, 60]

for score in scores:
    print(score)

for i, score in enumerate(scores):
    print(f"{i}番: {score}点")

total = 0
for score in scores:
    total += score
print(total)  # 410
