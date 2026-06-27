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


class Enemy(Character):
    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.hp = 150       # Enemy 専用の HP

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        print(f"{self.name}の攻撃！　{target.name}に{dmg}ダメージ！（残りHP: {target.hp}）")


hero = Character("勇者", attack_power=30)
boss = Enemy("ラスボス", attack_power=15)

while hero.is_alive() and boss.is_alive():
    hero.attack(boss)
    if boss.is_alive():
        boss.attack(hero)

if hero.is_alive():
    print(f"{hero.name}の勝利！")
else:
    print(f"{boss.name}の勝利！")
