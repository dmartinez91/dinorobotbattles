
class Robot:
    def __init__(self, name, weapon):
        self.robot_name = name
        self.health = 40
        self.robot_weapon = weapon

    # def __str__(self):
    #     return f' {self.robot_name} {self.health} {self.robot_weapon}' 
    
    def attack(self, dinosaur):
        dinosaur.health -= self.robot_weapon.AP
        print(f'{self.robot_name} used his {self.robot_weapon.weapon_name} and did {self.robot_weapon.AP} {dinosaur} has {dinosaur.health} remaining')

