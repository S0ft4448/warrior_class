from colorama import init, Fore, Style
from model.warrior_base import Warrior
# import random
import model.weapons as weapons
import time
from termcolor import colored
init()






class SwordMan(Warrior):
    
    def hello(self):
        super().hello()
        print("йоу васап ма бой")

    def hit(self, enemy):
        super().hit(enemy)
    
    def deadth(self):
        print(f"{self.name}ПЕРЕРАЖДЕНИЯ НЕ БУДЕТ ?")
        super().deadth()




class Archer(Warrior):
    def hello(self):
        super().hello()

        print("йоу гадем ")
    def hit(self, enemy):
        super().hit(enemy)

    def deadth(self):
        print(f"{self.name} как груба")
        super().deadth()

class Magek(Warrior):
    def __init__(self, name, health, arrmor, damege, weapon, magek_arrmor: int):
        super().__init__(name, health, arrmor, damege, weapon)
        self.magek_arrmor = magek_arrmor
    def hello(self):
        super().hello()
        print("здарова землечки")
    def hit(self, enemy):
        super().hit(enemy)
    def deadth(self):
        print(Fore.RED + f"{self.name}не стыдно убивать стареков ?" + Style.RESET_ALL)
        super().deadth()


class Goblen(Warrior):
    def __init__(self, name, health, arrmor, damege, weapon,drop:str):
        super().__init__(name, health, arrmor, damege, weapon)
        self.drop = drop
    def hello(self):
        super().hello()
        print("ыыы")
    def hit(self, enemy):
        super().hit(enemy)
    def deadth(self):
        print(f"{self.name} эта все твоя вина")
        super().deadth()


class Skelet(Warrior):
    def __init__(self, name, health, arrmor, damege, weapon,drop:str):
        super().__init__(name, health, arrmor, damege, weapon)
        self.drop = drop
    def hello(self):
        super().hello()
        print("hhh")
    def deadth(self):
        print(f"{self.name}i am.. am.. dead")
        super().deadth()
    def hit(sefl,enemy):
        super().hit(enemy)

