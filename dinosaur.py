
class Dinosaur():
    def __init__(self, name):
        self.dino_name = name
        self.health = 50
        self.bite = 5
    
    def attack(self, robot):
        robot.health -= self.bite