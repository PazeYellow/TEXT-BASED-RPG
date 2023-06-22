class Enemy:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def is_alive(self):
        return self.health > 0


class BasicEnemy(Enemy):
    def __init__(self):
        super().__init__("Basic Enemy", 10, 50)


class StrongEnemy(Enemy):
    def __init__(self):
        super().__init__("Strong Enemy", 20, 100)
