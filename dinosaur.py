
class Dinosaur:
    def __init__(self, name):
        self.dino_name = name
        self.health = 100
        self.bite = 5
    
    def __str__(self):
        return f' {self.dino_name} {self.health} {self.bite}'


    def attack(self, robot):
        robot.health -= self.bite

        print(f'{self.dino_name} attacked and did  {self.bite} damage to {robot.robot_name}. {robot.robot_name} has {robot.health} remaining')