from dinosaur import Dinosaur

class Herd():
    def __init__(self):
        self.dino_list = []
        self.create_herd()

    def create_herd(self):
        self.dino_list.append(Dinosaur('Petrie'))
        self.dino_list.append(Dinosaur('little foot'))
        self.dino_list.append(Dinosaur('Cera'))

