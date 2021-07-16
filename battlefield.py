from fleet import Fleet
from herd import Herd


class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.displayGreeting()    

    def displayGreeting(self):
        print('welcome to the simulation')

    def battle(self):
        self.dino_turn()
        self.robo_turn()
        # self.display_winners()

    def dino_turn(self, dinosaur):
        self.herd.dino_list[0].attack(self.fleet.robot_list[0])
        self.herd.dino_list[1].attack(self.fleet.robot_list[1])
        self.herd.dino_list[2].attack(self.fleet.robot_list[2])

    def robo_turn(self, robot):
        self.fleet.robot_list[0].attack(self.herd.dino_list[0])
        self.fleet.robot_list[1].attack(self.herd.dino_list[1])
        self.fleet.robot_list[2].attack(self.herd.dino_list[2])

    # def display_winners(self):
    #     while 
