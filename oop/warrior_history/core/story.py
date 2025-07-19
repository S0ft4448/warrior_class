from random import randint
import core.config as con
import model.warrior_class as war_class
import model.warrior_base as war_base
import model.weapons as wea

ways = ["gory", "rechk", "derevna", "les","idi na-#?"]
#          0        1        2         3        4
def main():
    print(f"our hero{con.main_hero.name} стоит на распутыи: ")
    print("kuda idti?: ")
    print("\n".join(f"{n+1}№ {w}"for n, w in enumerate(ways)))
    way = int(input('выбери номер (№) : ')) - 1
    print(f"{con.main_hero.name} направляется в {ways[way]}")
    if ways[way] == "gory":
        qaz = war_class.Archer("demon", 100, 12, 1, [wea.luk], 5)
        print(f"ты тут встретил {qaz.name}...\nON ANGRY -{qaz.angry}")
        if randint(0, 10) > qaz.angry:
            print("да ему поф!№; на тебя")
            fight = int(input("Напасть? (1 - да | 0 -нет ) : "))
            if fight:
                con.main_hero.fight(qaz)
            else:
                print("Прошел мимо и плюнул в спину")
        else: 
            print(f"{qaz.name} zloy daun хочет дратся\n{con.main_hero.name} хватайся за чтото там {con.main_hero.weapons[0].name}")
            qaz.fight(con.main_hero)


































    # con.main_hero.hello()
    # con.ar.hello()

    # con.main_hero.fight(con.ar)