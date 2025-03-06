# from turtle import Turtle, Screen
import turtle as t
import random

cheeku = t.Turtle()
cheeku.pensize(10)
cheeku.speed(0)

# dir = ["left", "right", "up", "down"]
# def movement(dir):
#     if dir== "up":
#         cheeku.left(90);
#         cheeku.forward(15);
#     if dir== "down":
#         cheeku.right(90);
#         cheeku.forward(15);
#     if dir== "left":
#         cheeku.left(180);
#         cheeku.forward(15);
#     if dir== "right":
#         cheeku.forward(15);

dir = [0, 90, 180, 270]
# colour = ["midnight blue", "dark sea green", "dark red", "dark orchid", "deep sky blue", "green yellow", "gold", "dim gray"]
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    # cheeku.pencolor(random.choice(colour))
    cheeku.pencolor(random_colour())
    move = random.choice(dir)
    # movement(move)
    cheeku.setheading(move)
    cheeku.forward(30)



screen = t.Screen()
screen.exitonclick()
