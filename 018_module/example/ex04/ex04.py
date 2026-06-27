"""
成績評価チェッカー
"""
# 点数リスト
scorelist = [95, 75, 30, 85]

# 関数：スコア判定
def gap(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


# 点数ごとにスコアを出力する
for score in scorelist:
    print(score,"点は、",gap(score))