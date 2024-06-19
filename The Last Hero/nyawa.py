import os

os.system("")

class Nyawa:
    waiting_symbol: str = "█"
    missing_symbol: str = "_"
    wall: str = "|"
    color_types: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue": "\33[34m",
        "green": "\033[92m",
        "default": "\033[0m"
    }

    def __init__(self, entity, length: int = 20, colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.full_health = entity.health_max
        self.current_health = entity.health
        self.colored = colored
        self.color = self.color_types.get(color) or self.color_types["default"]

    def update(self) -> None:
        self.current_health = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_health / self.full_health * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.nama} Health: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.wall}"
              f"{self.color if self.colored else ''}"
              f"{remaining_bars * self.waiting_symbol}"
              f"{lost_bars * self.missing_symbol}"
              f"{self.color_types['default'] if self.colored else ''}"
              f"{self.wall}")
