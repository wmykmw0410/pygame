class Character():
    def __init__(self, name, attack_power):
        self.name         = name
        self.hp           = 100
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name}の攻撃! {target.name}に{self.attack_power}ダメージ!(残りHP: {target.hp})")

    def is_alive(self):
        return self.hp > 0


class Enemy(Character):
    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.hp = 150       # Enemy 専用の HP

    def attack(self, target):
        dmg = int(self.attack_power * 1.5)
        target.hp -= dmg
        print(f"{self.name}の攻撃! {target.name}に{dmg}ダメージ!(残りHP: {target.hp})")


player = Character("勇者", attack_power=30)
enemy = Enemy("スライム", attack_power=15)

while player.is_alive() and enemy.is_alive():
    player.attack(enemy)
    if enemy.is_alive():
        enemy.attack(player)

if player.is_alive():
    print(f"{player.name}の勝利!")
else:
    print(f"{enemy.name}の勝利!")
