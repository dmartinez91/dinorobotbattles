from fleet import Fleet
# from herd import Herd


class battle():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.displayGreeting()    

    def displayGreeting(self):
        print('welcome to the simulation')

    def battle(self):
        
    # def dino_turn(self, dinosaur):

    def robo_turn(self, robot):
        self.fleet.robot_list[0].attack(self.herd.dino_list[0])


