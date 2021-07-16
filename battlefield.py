# from robot import Robot
# from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.displayGreeting()
        self.battle()
        self.winner()   

    def displayGreeting(self):
        print('WELCOME TO DINO VS ROBOTS, WHO WILL WIN?!')

    def battle(self):
        i = 0
        for i in range(len(self.herd.dino_list)):
            while self.herd.dino_list[i].health != 0 and self.fleet.robot_list[i].health != 0:
                self.dino_turn()
                self.robo_turn()
        # self.display_winners()

    def dino_turn(self):
        self.herd.dino_list[0].attack(self.fleet.robot_list[0])
        self.herd.dino_list[1].attack(self.fleet.robot_list[1])
        self.herd.dino_list[2].attack(self.fleet.robot_list[2])

    def robo_turn(self):
        self.fleet.robot_list[0].attack(self.herd.dino_list[0])
        self.fleet.robot_list[1].attack(self.herd.dino_list[1])
        self.fleet.robot_list[2].attack(self.herd.dino_list[2])

    def winner(self):
        i = 0
        for i in range(len(self.fleet.robot_list)):
            if self.fleet.robot_list[i].health == 0:
                print(f'{self.fleet.robot_list[i].robot_name} has been defeated!!')
            else:
                print(f'{self.herd.dino_list[i].dino_name} has been defeated!')
            

        
    # create method that checks to see the value of health and then eliminates combatents

