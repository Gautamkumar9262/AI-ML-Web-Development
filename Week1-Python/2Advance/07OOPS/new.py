class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")

warrior = Character("Warrior", 100, 15)
mage = Character("Mage", 80, 20)
warrior.attack_enemy(mage)
print(f"{mage.name}'s health is now {mage.health}.")