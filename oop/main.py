import turtle
givem_me_money = "ye mayki"

class Animal:
    def __init__(
        self,
        name: str,
        color: tuple[int, int, int],
        song: str,
        legs: int
    ):
        self.name = name
        self.color = color
        self.count_legs = legs
        self.song = song
        

    def get_name(self):
        return self.name

    def hello(self):
        print(f"object name: {self.name} class`s {self.__class__.__name__} say: {self.song}, color: {self.color}, legs: {self.count_legs}")

class KAT(Animal):
    
    def __init__(
        self,
        name,
        color,
        song,
        legs,
        lives: int
    ):
        super().__init__(name, color, song, legs)
        self.lives = lives
    
    def mur_mur(self):
        print(f"mur mur")
    def dead(self):
        self.lives = self.lives - 1
        print(f"у кота -1 жизнь, осталось {self.lives}")

anim = Animal("dima", (23, 4, 7), "ez mid", 4)
anim.hello()
pikun = KAT("sasha yahsa", (24, 4 ,5 ), "bleeee ble ble", 4,4)
# result = anim.hello()
pikun.hello()
print(pikun.__class__.__bases__)
pikun.mur_mur()
pikun.dead()
# print(result)
# a = 1
# b = None
# def gadem():
#     pass
# print(type(print))
# print(type(t))
# print(type(anim))
# print(type(a))
# print(type(b))
# print(type(gadem))
# print(anim.__class__.__base__)
# str()

