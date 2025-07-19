from abc import ABC, abstractmethod
import time
from colorama import init, Fore, Style
from termcolor import colored

class Weapon:
    def __init__(
        self,
        name: str,
        damage: int,
        arrmor: int
    ):
        self.name = name
        self.damage = damage
        self.arrmor = arrmor


    def __call__(self, *args, **kwds):
        return self.damage


class Warrior(ABC):
    def __init__(
        self,
        name: str,
        health: int,
        arrmor: int,
        damege: float,
        weapons: list[Weapon],  # <-- теперь список оружий
        angry: int = 0
    ):
        self.name = name
        self.health = health
        self.base_arrmor = arrmor
        self.base_damege = damege
        self.weapons = weapons
        self.isLivefe = True
        self.position = None
        self.angry = angry

        # Подсчёт итогового урона и брони от оружий
        self.damege = damege * sum(w.damage for w in weapons)
        self.arrmor = arrmor + sum(w.arrmor for w in weapons)



    @abstractmethod
    def deadth(self):
        self.isLivefe = False
        print(f"{self.name} уходит на тот свет")



    def statick(self):
        weapon_names = ", ".join(w.name for w in self.weapons)
        
        print(
            colored("static", "white"),
            colored(f"{self.name}", "yellow"),
            colored("class", "white"),
            colored(f"{self.__class__.__name__}", "green"),
            "\n" +
            colored("Weapons: ", "white") + colored(weapon_names, "magenta") + "\n" +
            colored("HP: ", "white") + colored(f"{self.health}", "green") + "  " +
            colored("AR: ", "white") + colored(f"{self.arrmor}", "cyan") + "  " +
            colored("DMG: ", "white") + colored(f"{self.damege}", "red")
        )


    @abstractmethod
    def hello(self):
        print(f"игрок {self.name} класса {self.__class__.__name__}.")





    def __hit(self, enemy: "Warrior"):
        if enemy.arrmor > 0:
            enemy.arrmor = enemy.arrmor - self.damege
            if enemy.arrmor < 0:
                enemy.health = enemy.health - abs(enemy.arrmor)
                enemy.arrmor = 0
        else:
            enemy.health = enemy.health - self.damege

    @abstractmethod
    def hit(self,enemy: "Warrior"):
        self.__hit(enemy)
        enemy.statick()

    def fight(self,enemy: "Warrior"):
        print("\033[91m---------Драка\033[0m")
        time.sleep(1.5)
        print(Fore.GREEN + self.name + Style.RESET_ALL,"----напал-на---",Fore.RED + enemy.name + Style.RESET_ALL)
        time.sleep(1)
        while True:
            self.hit(enemy)
            time.sleep(1)
            if enemy.health <= 0:
                enemy.deadth()
                time.sleep(1)
                break
            enemy.hit(self)
            time.sleep(1)
            if self.health <= 0:
                self.deadth()
                time.sleep(1)
                break


