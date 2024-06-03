from random import randrange as rnd
from tkinter import *
from random import choice


root = Tk()
canvas = Canvas(root, width=600, height=400)
canvas.pack()


class Ball:
    def __init__(self, color):
        self.x = 200
        self.y = 500
        self.r = 2.4
        self.vx = 6
        self.ay = 0
        self.vy = -1
        self.color = color
        self.live = 50
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color,
            width=0,
        )
        self.div = 0

    def set_coords(self):
        canvas.coords(
            self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r
        )

    def divide(self, n=3):
        global balls

        for z in range(n):
            balls += [Ball(random_color())]
            balls[-1].div = 1
            balls[-1].x = self.x
            balls[-1].y = self.y
            balls[-1].vx = self.vx + n - z * 2
            balls[-1].vy = self.vy + rnd(10) / 4
            balls[-1].ay = 0.2
        self.kill()

    def set_minus_r(self):
        self.r -= 0.04
        if self.r <= 0.5:
            self.kill()
        else:
            canvas.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
            )

    def kill(self):
        global balls

        balls.pop(balls.index(self))
        canvas.delete(self.id)

    def move(self):
        if self.vy > 0 and self.y > rnd(300, 400):
            self.kill()
        else:
            if self.y < 300 and not self.div and not rnd(5):
                self.divide(3)
            else:
                if self.vy > 0:
                    self.set_minus_r()

                self.y += self.vy
                self.vy += self.ay
                self.x += self.vx
                if self.x > (800 - self.r):
                    self.vx = -self.vx // 2
                    self.x = 800 - self.r - 1
                self.set_coords()


def random_color():
    colors = [
        "white",
        "black",
        "gray",
        "brown",
        "red",
        "orange",
        "yellow",
        "lime",
        "green",
        "cyan",
        "blue",
        "navy",
        "magenta",
        "purple",
        "violet",
        "pink",
    ]
    return choice(colors)


balls = []
k1 = k2 = k = 0
vy = 0
vx = 0
d = 30
dd = 30
ddd = 2

while 1:
    if k > d:
        vy = rnd(3)
        d = rnd(40, 45)
        k = 0
    k += 1

    if k1 > dd:
        vx = rnd(-5, 5)
        dd = rnd(40, 50)
        k1 = 0
    k1 += 1

    if k2 > ddd:
        for zz in range(rnd(-5, 0), rnd(6), 3):
            balls += [Ball(random_color())]
            balls[-1].vx = (zz + vx) / 8
            balls[-1].vy = -8 + vy + rnd(20) / 12
        k2 = 0

    k2 += 1
    for b in balls:
        b.move()

    canvas.update()
