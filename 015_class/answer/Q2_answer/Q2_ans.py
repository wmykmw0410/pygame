class Character():
    def __init__(self, name, attack_power):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name}の攻撃！　{target.name}に{self.attack_power}ダメージ！（残りHP: {target.hp}）")

    def is_alive(self):
        return self.hp > 0


hero  = Character("勇者", attack_power=30)
demon = Character("魔王", attack_power=20)

while hero.is_alive() and demon.is_alive():
    hero.attack(demon)
    if demon.is_alive():
        demon.attack(hero)

if hero.is_alive():
    print(f"{hero.name}の勝利！")
else:
    print(f"{demon.name}の勝利！")
