from turtle import Turtle  # from turtle module importing Turtle class
from turtle import Screen
import random

timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('purple')

# draw a square
'''
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
'''

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# dashed line
'''
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
'''

# # square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# # pentagon
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72)

colours = ["midnight blue", "dark sea green", "dark red", "dark orchid", "deep sky blue", "green yellow", "gold", "dim gray"]
for n in range(3,11):
    timmy.color(random.choice(colours))
    angle = 360/n
    for _ in range(n):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()


#### simple import ####
# import <module_name>, creating object -> var/obj_name = <module_name>.<class_name>
# ex. : import turtle, timmy = turtle.Turtle()

#### from import ####
# from <module_name> import <Thing in the module to be imported>
# ex. : from turtle import Turtle

# from <module_name> import *   --> * means everything, so everything in the module can be imported using this syntax


#### alias modules ####
# import turtle as t
