import turtle
import time


wn = turtle.Screen()
wn.setup(1200, 700, 0, 0)
wn.bgpic("Street9(4).gif")

turtle.tracer(2)

turtle.penup()
turtle.hideturtle()
s = turtle.Shape("compound")


def polygon(x1, y1, x2, y2, x3, y3, x4, y4, clr1, clr2):
    poly = ((x1, y1), (x2, y2), (x3, y3), (x4, y4))
    s.addcomponent(poly, clr1, clr2)


def circles(x, y, r, clr1, clr2):
    turtle.up()
    turtle.goto(x, y - r)
    # turtle.down()
    turtle.begin_poly()
    turtle.circle(r)
    turtle.end_poly()
    m = turtle.get_poly()
    s.addcomponent(m, clr1, clr2)


polygon(0, 15, 10, 30, 55, 30, 55, 15, "purple", "black")
polygon(15, 30, 30, 50, 30, 30, 30, 30, "violet", "black")
polygon(30, 30, 30, 50, 55, 50, 55, 30, "blue", "black")
polygon(55, 30, 55, 50, 80, 50, 80, 30, "blue", "black")
polygon(55, 5, 55, 30, 80, 30, 80, 15, "crimson", "black")
polygon(80, 15, 80, 50, 100, 30, 100, 30, "orange red", "black")
polygon(80, 15, 100, 30, 130, 30, 130, 15, "green yellow", "black")
polygon(130, 15, 130, 30, 155, 15, 155, 15, "green", "black")
polygon(130, 0, 130, 15, 155, 15, 140, 0, "red", "black")
polygon(30, -10, 30, 15, 130, 15, 130, -10, "coral", "black")
polygon(20, -10, 0, 15, 20, 15, 20, 15, "lawn green", "black")
polygon(105, 25, 105, 55, 107, 55, 107, 25, "black", "black")

circles(30, -2, 20, "green", "black")
circles(30, -2, 10, "forest green", "black")
circles(30, -2, 5, "blue", "black")
circles(120, -2, 20, "green", "black")
circles(120, -2, 10, "forest green", "black")
circles(120, -2, 5, "blue", "black")

polygon(62.5, 50, 67.5, 53, 72.5, 53, 77.5, 50, "navy", "black")
polygon(67.5, 53, 60, 60, 80, 60, 72.5, 53, "red", "red")
polygon(60, 60, 62.5, 65, 77.5, 65, 80, 60, "red", "red")
polygon(60, 65, 70, 80, 80, 65, 80, 65, "blue", "blue")
polygon(66, 56, 66, 58, 74, 58, 74, 56, "gold", "gold")
polygon(69, 60, 69, 62, 72, 62, 72, 60, "light blue", "light blue")
polygon(58, 60, 58, 62, 60, 62, 60, 60, "brown", "brown")
polygon(80, 60, 80, 62, 82, 62, 82, 60, "brown", "brown")

circles(65, 62, 1, "black", "black")
circles(75, 62, 1, "black", "black")

wn.addshape("car", s)
car = turtle.Turtle(shape="car")
car.penup()
car.tilt(90)
car.hideturtle()
car.goto(-400, 0)
car.shapesize(0.6)
car.hideturtle()
car.goto(-400, 150)
car.showturtle()
turtle.tracer(50)
# for m in range(1):
while True:
    car.showturtle()
    car.goto(0, -250)
    car.setheading(0)
    for m in range(360):
        car.circle(250, 1)
        time.sleep(0.008)
