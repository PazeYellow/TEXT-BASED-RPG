import random
from enemy import BasicEnemy, StrongEnemy

class Area:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def get_random_enemy(self):
        return random.choice(self.enemies)


class AreaManager:
    def __init__(self):
        self.areas = self.create_areas()

    def create_areas(self):
        areas = {
            "kingdom": Area("Kingdom", [BasicEnemy()]),
            "forest": Area("Forest", [BasicEnemy(), StrongEnemy()]),
            "cave": Area("Cave", [StrongEnemy()])
        }
        return areas

    def get_area(self, area_name):
        return self.areas.get(area_name.lower())
