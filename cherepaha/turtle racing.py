import turtle
import random 
from turtle import Turtle

finish_line_x = 300

turtles:list[Turtle] = []
screen = turtle.Screen()
screen.setup(width=724, height=504)
screen.title("Гонки черепах")
screen.listen()


line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line_x, -250)
line.pendown()
line.pensize(4)
line.color("black")
line.setheading(90)  
line.forward(500)



def click(x :float, y: float, t: Turtle):
    print(x, y, t)
    print(t.color()[0])
    t.goto(t.xcor()+10,t.ycor())

colors = ['red', 'blue', 'green', 'orange']
turtles = []

start_y = -100
for color in colors:
    t = turtle.Turtle(shape='turtle')
    t.onclick(lambda x, y, t=t: click(x,y,t))
    t.color(color)
    t.penup()
    t.goto(-350, start_y)
    start_y += 60
    turtles.append(t)

race_over = False

while not race_over:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= finish_line_x:
            race_over = True
            print(f"{t.color()[0]} черепаха победила!")
            t.goto(0,0)
            t.write(
                "han i'd win",
                True,
                "center",
                ("Arial", 24, "normal"))
            break  






# i am, am egoisto ITOSHI RIN 
















turtle.done()