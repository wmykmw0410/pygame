"""Q3. 敵クラスを継承で作る

Q2 で作った Character を親クラスとして、Enemy クラスを作ろう。

step1. Enemy(Character) を定義する
       ・__init__(self, name, attack_power) で super() を呼ぶ
       ・Enemy 専用のプロパティとして hp = 150 を設定する

step2. attack() をオーバーライドする
       ・攻撃力を 1.5 倍にして target.hp を減らす（int に変換する）
       ・攻撃結果を表示する

step3. 以下で戦わせる
       ・hero = Character("勇者", attack_power=30)
       ・boss = Enemy("ラスボス", attack_power=15)
"""

# Character クラスを定義する（Q2 と同じ）

    # __init__: name, hp = 100, attack_power を初期化する

    # attack(target): target.hp を attack_power 分減らし、結果を表示する

    # is_alive(): hp > 0 なら True を返す


# Enemy クラスを定義する（Character を継承）

    # __init__: super() を呼び、hp = 150 を設定する

    # attack() をオーバーライド: 攻撃力を 1.5 倍にして攻撃する


# 動作確認
