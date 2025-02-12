import os
os.system('cls')

from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract("image.jpg", 30)

lst = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

# for i in colors:
#     lst.append(tuple(i.rgb))
# print(lst)

obj = Turtle()
screen = Screen()
screen.colormode(255)
# screen.screensize(2000,2000)
# obj.setheading(225)
# obj.penup()
# obj.forward(300)
# obj.setheading(0)
obj.speed(0)
obj.hideturtle()
obj.penup()
obj.setpos(-250,-200)
for j in range(10):
    for i in range(10):
        obj.pendown()
        obj.dot(20, random.choice(lst))
        obj.penup()
        obj.forward(50)
    obj.setpos(-250,(obj.pos()[1]+50))


screen.exitonclick()