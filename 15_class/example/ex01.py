class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def take_damage(self, amount):
        self.hp -= amount

    def show_status(self):
        print(f"{self.name} HP: {self.hp}")


player = Player("勇者", 100)
player.show_status()      # 勇者 HP: 100

player.take_damage(30)
player.show_status()      # 勇者 HP: 70

player.take_damage(20)
player.show_status()      # 勇者 HP: 50
