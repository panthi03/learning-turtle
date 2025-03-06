import turtle as t
import random

t.colormode(255)

katori = t.Turtle()
katori.speed(0)

def colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


def spirograph(gap):
    for _ in range(360 // gap):
        katori.pencolor(colour())
        katori.circle(100)
        # katori.right(5)
        # katori.forward(10)
        katori.setheading(katori.heading() + gap)


spirograph(5)

screen = t.Screen()
screen.exitonclick()