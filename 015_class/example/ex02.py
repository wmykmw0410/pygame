class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def take_damage(self, amount):
        self.hp -= amount

    def show_status(self):
        print(f"{self.name} HP: {self.hp}")


# インスタンスはそれぞれ独立している
p1 = Player("勇者",    100)
p2 = Player("魔法使い",  80)

p1.take_damage(30)       # p1 だけ HP が減る
p1.show_status()         # 勇者 HP: 70
p2.show_status()         # 魔法使い HP: 80

print("---")

# リストで複数まとめて管理する
party = [Player("勇者", 100), Player("魔法使い", 80), Player("戦士", 120)]

for p in party:
    p.take_damage(10)    # 全員まとめてダメージ

for p in party:
    p.show_status()
