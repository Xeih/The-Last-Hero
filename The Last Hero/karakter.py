from senjata import Claws, Sword
from nyawa import Nyawa
import random

class Karakter:
    def __init__(self, nama: str, health: int) -> None:
        self.nama = nama
        self.health = health
        self.health_max = health
        self.weapon = Claws

    def attack(self, target) -> None:
        self.weapon.use()
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.nyawa.update()
        print(f"{self.nama} gives {self.weapon.damage} damage to {target.nama} with {self.weapon.nama}")

class Ksatria(Karakter):
    def __init__(self, nama: str, health: int) -> None:
        super().__init__(nama=nama, health=health)
        self.default_weapon = self.weapon
        self.nyawa = Nyawa(self, color="blue")

    def use(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.nama} uses {self.weapon.nama}!")

    def drop(self) -> None:
        print(f"{self.nama} drops {self.weapon.nama}!")
        self.weapon = self.default_weapon

class TacetDiscord(Karakter):
    def __init__(self, nama: str, health: int, weapons: list) -> None:
        super().__init__(nama=nama, health=health)
        self.weapons = weapons
        self.weapon = random.choice(self.weapons)
        self.nyawa = Nyawa(self, color="red")

    def attack(self, target) -> None:
        self.weapon = random.choice(self.weapons)
        super().attack(target)


class Phoenix(Karakter):
    def __init__(self, nama: str, health: int, weapons: list) -> None:
        super().__init__(nama=nama, health=health)
        self.weapons = weapons
        self.weapon = random.choice(self.weapons)
        self.nyawa = Nyawa(self, color="orange")

    def attack(self, target) -> None:
        self.weapon = random.choice(self.weapons)
        super().attack(target)

