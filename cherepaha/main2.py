import turtle
from turtle import Turtle
import random
import colorsys
# t1 = Turtle("turtle")
# t2 = Turtle("turtle")
# t3 = Turtle("turtle")
# t4 = Turtle("turtle")
turtles = [Turtle() for _ in range(72)]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
dis = 100
def move(t: Turtle):
    global dis
    for i in range(4):
        t.forward(dis)
        t.right(90)
    dis = dis+30

positions = [(-200, 200), (200, 200), (200, -200), (-200, -200)]
for i, t in enumerate(turtles):
    t.penup()
    t.goto(positions[3])
    t.pendown()
    
# def sayk_move(t_list: list[Turtle]):
#     dis = 100
#     unique_colors = random.sample(colors, len(t_list))
#     for i, t in enumerate(t_list):
#         t.color(unique_colors[i])
#         for _ in range(4):
#             t.forward(dis)
#             t.right(90)
#         dis += 30


def round_pos(t_list: list[Turtle]):
    step_angle = 360 / len(t_list)
    angle = 0
    for t in t_list:
        t.left(angle)
        angle = angle + step_angle
        t.forward(100)
turtle.colormode(255)  # включаем RGB режим


def drow(t_list: list[Turtle]):
    ford = 5
    count = 0
    lefft = 4
    while count < 100:
        count = count+1
        for t in t_list:
            t.forward(ford)
            t.left(lefft)
        ford = ford+5
        lefft = lefft+2

def rainbow_gradient(items):
    n = len(items)
    colors = []
    for i in range(n):
        hue = i / n 
        r, g ,b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)    
        hex_color = (int(r*255), int(g*255), int(b*255)) 
        colors.append(hex_color)
    return colors

def set_color(t_list: list[Turtle]):
    colors = rainbow_gradient(t_list)
    for n, t in enumerate (t_list):
        turtle.colormode(255)
        t.speed(0)
        t.color(colors[n])
        t.pensize(10)


set_color(turtles)
round_pos(t_list=turtles)
drow(turtles)
# sayk_move(turtles)
# list(map(move, turtles))
# move(turtles[1])
# sayk_move(turtles)
turtle.done()
# моя функцыя по примеру функцый sayk_move должна каждой черепашке давать рандомный цвет из списка colors
# для каждой черепашке цвет должен быть уникальный 