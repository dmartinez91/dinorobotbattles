from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        
        self.robot_list = []
        self.create_fleet()
       

    def create_fleet(self):
        self.robot_list.append(Robot("Bender",Weapon('Ray gun', 9)))
        self.robot_list.append(Robot("R2-D2", Weapon('Cattle prod', 3)))
        self.robot_list.append(Robot('Mecha Godzilla', Weapon('lasers', 8)))

   


