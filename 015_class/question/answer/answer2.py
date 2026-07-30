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


player = Character("勇者", attack_power=30)
enemy  = Character("スライム", attack_power=20)

while player.is_alive() and enemy.is_alive():
    player.attack(enemy)
    if enemy.is_alive():
        enemy.attack(player)

if player.is_alive():
    print(f"{player.name}の勝利!")
else:
    print(f"{enemy.name}の勝利!")
