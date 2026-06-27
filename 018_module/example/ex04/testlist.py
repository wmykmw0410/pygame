"""「mycalc.py」からgap関数をimportし、成績を評価する"""
#「mycalc.py」をimport
import mycalc

# 点数リスト
scorelist = [95, 75, 30, 85]

# 点数ごとにスコアを出力する
for score in scorelist:
    print(score,"点は、",mycalc.gap(score))