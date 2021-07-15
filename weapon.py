class Weapon():
    def __init__(self, name, attack_power):
        self.weapon_name = name
        self.AP = attack_power
    def __str__(self):
        return f'{self.AP}'
