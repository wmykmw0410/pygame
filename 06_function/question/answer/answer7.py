"""ゲームのスコアを管理するグローバル変数 score(初期値0) を用意し、
呼ぶたびに10点加算する関数 add_score を作成せよ（global宣言を使うこと）

呼び出し方：add_score() を2回呼んだ後の score を表示する

出力結果：
        20
"""

score = 0

def add_score():
    global score   # global をつけないと UnboundLocalError
    score += 10

add_score()
add_score()
print(score)  # 出力: 20
