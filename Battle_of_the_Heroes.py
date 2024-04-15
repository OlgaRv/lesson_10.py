import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        special_chance = random.randint(1,10)  # Шанс на внезапную атаку (от 1 до 10)
        dodge_chance = random.randint(1,10)  # Шанс на избежание атаки (от 1 до 10)

        if special_chance <= 3:  # 30% шанс на внезапную атаку
            self.special_attack(other)
        elif dodge_chance <= 2:  # 20% шанс на избежание атаки
            print(f"Игрок {self.name} избежал внезапной атаки!")
        else:
            random_attack_power = random.randint(-5, 5)
            other.health -= (self.attack_power + random_attack_power)

    def special_attack(self, other):
        # Реализация внезапной атаки
        print(f"Игрок {self.name} применил внезапную атаку!")
        other.health -= self.attack_power * 2

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"У игрока {self.player.name} уровень здоровья такой: {self.player.health}")
            print(f"У игрока {self.computer.name} уровень здоровья такой: {self.computer.health}")

            self.player.attack(self.computer)
            print(f"Игрок {self.player.name} атакует {self.computer.name}")

            if not self.computer.is_alive():
                print(f"Игрок {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            print(f"Игрок {self.computer.name} атакует {self.player.name}")

            if not self.player.is_alive():
                print(f"Игрок {self.computer.name} победил!")
                break

player_name = input("Введите имя вашего игрока: ")
game = Game(player_name)
game.start()