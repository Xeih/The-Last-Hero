class Weapon:
    def __init__(self, nama: str, weapon_type: str, damage: int, value: int, durability: int) -> None:
        self.original_nama = nama
        self.nama = nama
        self.weapon_type = weapon_type
        self.original_damage = damage
        self.damage = damage
        self.value = value
        self.durability = durability

    def use(self) -> None:
        if self.durability > 0:
            self.durability -= 1
            if self.durability == 0:
                self.nama = f"Broken {self.original_nama}"
                self.damage = self.original_damage // 2

Sword = Weapon(nama="Sword", weapon_type="Sharp", damage=50, value=50, durability=50)
FireBreath = Weapon(nama="Fire Breath", weapon_type="Magic", damage=100, value=0, durability=float('inf'))
Claws = Weapon(nama="Claws", weapon_type="Sharp", damage=30, value=0, durability=float('inf'))
Axe = Weapon(nama="Axe", weapon_type="Sharp", damage=60, value=50, durability=40)
SamuraiSword = Weapon(nama="Samurai Sword", weapon_type="Sharp", damage=70, value=70, durability=60)
