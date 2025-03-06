import turtle as t
import random
# import colorgram
#
#
# colours = colorgram.extract("image.jpg", 30)
#
# def rgb_col(i):
#     col = colours[i].rgb
#     r = col.r
#     g = col.g
#     b = col.b
#     return (r, g, b)
#
# for i in range(30):
#     colours[i] = rgb_col(i)
#
# print(colours)

colour_palette = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
t.colormode(255)

picaso = t.Turtle()
picaso.speed('fastest')
picaso.penup()
picaso.hideturtle()

def hirst():
    for _ in range(10):
        picaso.dot(20, random.choice(colour_palette))
        picaso.forward(50)

for i in range(-5,5):
    picaso.setx(-250)
    picaso.sety(i*50)
    hirst()


screen = t.Screen()
screen.exitonclick()