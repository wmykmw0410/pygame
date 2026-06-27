"""
シャッフルされたトランプの山札から、
シェルから入力された数字分だけカードを引き、
結果を出力するプログラムを作成する

ただし、カードを引く部分はdraw_cards関数にまとめ、
引数としてdeck(山札)とnum_cards(引く枚数)を指定する
また、シェルからの入力が無効であった場合、適切に例外処理せよ
"""

import random

# トランプのスートとランクを定義
suits = ["ハート", "ダイヤ", "クラブ", "スペード"]

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# 関数：カードを引く
def draw_cards(deck, num_cards):

    # 空の配列draw_cardsを用意する
    draw_cards = []

    # シェルから入力された枚数分、繰り返す
    for _ in range(num_cards):

        # deckからpopしたカードをdraw_cardsに追加する
        draw_cards.append(deck.pop())
    
    # 戻り値：draw_cards
    return draw_cards

    
# トランプの山札を作成
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f"{suit}の{rank}")


# 山札をシャッフルする
random.shuffle(deck)

# 例外処理
try:

    # 引く枚数を入力させる
    num_cards = int(input("引く枚数を入力してください:"))

    # カードが52枚より多いときは
    if num_cards > 52:
        # 「53枚以上は引けません」と出力する
        print("53枚以上は引けません")

        # num_cardsに0を代入する
        num_cards = 0

# 無効な入力の時は
except ValueError:

    # 「無効な入力です」と出力する
    print("無効な入力です")

    # num_cardsに0を代入する
    num_cards = 0

# 指定された枚数分だけカードを引く
draw_cards = draw_cards(deck, num_cards)

# 引いたカードを表示
print("引いたカード：")
for card in draw_cards:
    print(card)