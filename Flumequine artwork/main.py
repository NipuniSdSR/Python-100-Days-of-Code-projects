# extract colors of the image by using colorgram package and save it as list of tuples
# import colorgram
#
# colors = colorgram.extract('image.jpg', 40)
#
#
# def exact_colors(color_obj):
#     colors = []
#     for color in color_obj:
#         exact_color = color.rgb
#         r = exact_color.r
#         g = exact_color.g
#         b = exact_color.b
#         colors.append((r, g, b))
#
#     return colors
#
#
# colors = exact_colors(colors)
# print(colors)
import random
import turtle

color_list = [
    (215, 228, 243), (241, 250, 243), (117, 162, 212), (210, 153, 95), (132, 91, 53),
    (27, 109, 177), (192, 130, 175), (205, 75, 123), (15, 25, 87), (96, 106, 194), (42, 39, 138), (238, 201, 96),
    (167, 164, 234), (231, 157, 202), (176, 12, 40), (156, 53, 103), (121, 165, 128), (55, 4, 31), (158, 221, 152),
    (231, 85, 41), (203, 136, 32), (72, 170, 100), (31, 152, 198), (251, 218, 0), (7, 97, 107), (166, 205, 213),
    (14, 51, 48), (96, 61, 25), (63, 114, 102), (224, 178, 167), (19, 94, 91), (154, 26, 23), (80, 36, 31)
]

# create the damien Herts dot painting using turtle packaege
# dot size=20
# gap between two dots = 50
# image must contain 10 dots horizontally and 10 dots vertically

import turtle as turtle_module

import random
turtle_module.colormode(255)


timmy = turtle_module.Turtle()
screen = turtle_module.Screen()
no_of_dots =10
dot_size = 20
dot_gap = 50

#my way of drawing the painting
timmy.penup()
timmy.hideturtle()
timmy.setposition(-240, -240)
for _ in range(no_of_dots):
    start_x_position = timmy.xcor()

    for _ in range(no_of_dots):
        timmy.dot(dot_size, random.choice(color_list))

        timmy.forward(dot_gap)


    timmy.setposition(start_x_position, timmy.ycor()+50)



# # angela way of drawing the painting
# timmy.speed('fastest')
# #since the dots are going out of the window set start position left to the origin
# #direction 225 degree
# timmy.setheading(225)
# #go along that direction just for 225 distance
# timmy.penup()
# timmy.hideturtle()
# timmy.forward(325)
# #set direction to east
# timmy.setheading(0)
#
# no_of_dots = 100
#
# for dot_count in range(1, no_of_dots+1):
#     timmy.dot(dot_size, random.choice(color_list))
#
#     timmy.forward(50)
#
#     if dot_count%10 == 0:
#
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(180)
#         timmy.forward(500)
#         timmy.setheading(0)

screen.exitonclick()
