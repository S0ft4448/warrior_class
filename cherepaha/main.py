import turtle

t = turtle.Turtle("turtle")
m = turtle.Turtle("square")
b = turtle.Turtle("circle")
g = turtle.Turtle("triangle")
t.speed(0)
m.speed(0)
b.speed(0)
g.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
blacks = ["Black", "DarkSlateGray", "DimGray", "Gray","LightSlateGray", "SlateGray", "DarkGray"]
greens = ["Green", "Lime", "LimeGreen", "ForestGreen", "SeaGreen","MediumSeaGreen", "DarkSeaGreen", "YellowGreen", "OliveDrab","DarkOliveGreen", "Olive", "SpringGreen", "MediumSpringGreen","PaleGreen", "LightGreen", "Chartreuse", "GreenYellow","Lawngreen", "Turquoise", "MediumAquamarine", "Aquamarine"]
blubers = ["Aqua", "Cyan", "LightCyan", "PaleTurquoise", "Aquamarine","Turquoise", "MediumTurquoise", "DarkTurquoise", "CadetBlue", "SteelBlue", "MidnightBlue", "Navy"]
t.forward(100)
m.left(90)
m.forward(100)
b.right(90)
b.forward(100)
g.back(100)
for i in range(500):
    t.color(colors[i % len(colors)])
    t.forward(100)
    
    t.right(90)
    
    m.color(blubers[i % len(blubers)])
    m.forward(20)
    m.right(25)
    
    b.color(greens[i % len(greens)])
    b.forward(30)
    b.right(20)

    g.color(blacks[i % len(blacks)])
    g.forward(50)
    g.right(150)


turtle.done()