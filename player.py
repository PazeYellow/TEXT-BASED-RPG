class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        self.enemies_killed = 0
        self.level = 1

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount

    def receive_gold(self, amount):
        self.gold += amount

    def increase_enemies_killed(self):
        self.enemies_killed += 1

    def level_up(self):
        self.level += 1
