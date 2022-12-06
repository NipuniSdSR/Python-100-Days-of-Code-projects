# from turtle import Screen, Turtle
# import time
#
# # todo : Create the playing window
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('My Snake Game')
#
# screen.tracer(0)  # visibility off. by using update we can show the object when its suppose to
#
# # Todo 1: Create a snake body
# '''
# Create 3 turtles and position them in 0,0 then other two are left to it
# Each turtle should be a white square (default size:20x20)
# '''
#
# # turtle1 = Turtle("square")
# # turtle1.color('white')
# #
# # turtle2 = Turtle(shape="square")
# # turtle2.color('white')
# # turtle2.setx(-20)
# #
# # turtle3 = Turtle(shape="square")
# # turtle3.color('white')
# # turtle3.goto(-40,0)
#
# '''
# To make a coherent structure segment array was created
# '''
#
# segments = []
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_positions:
#     new_segment = Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()  # not to create line on the trail of the object
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# # Todo 2: Move the snake across the window
#
# game_is_on = True
#
# while game_is_on:
#
#     # # check 1
#     # # move each segment 20 pixels forwards
#     #
#     # '''
#     # movement is too fast. import the time module to slow it down
#     # '''
#     # for seg in segments:
#     #     seg.forward(20)
#     #     screen.update() # show the object here
#     #     time.sleep(1) #1s delay at each segment movements. what we need is all 3 delay same time
#
#     # # check 2
#     # screen.update()  # show the object here
#     # time.sleep(1)  # all 3 delay same time
#     # for seg in segments:
#     #     seg.forward(20)
#
#     # screen.update()
#     # time.sleep(0.1)
#     # # check 3
#     # '''
#     # To solve the all three segments link together we substitute 3->2, 2->1 then 1-> new move
#     #
#     # i.e: loop through last to first in reverse order
#     # '''
#     # # to go reverse order of a array : range (start= 10, end = 0, step= -1) <- step -1  make the reverse order
#     # for seg_num in range(len(segments) - 1, 0, -1):
#     #     # previous segment cordinates if 3 get the movement of 2 , this is coordinates of 2
#     #     new_x = segments[seg_num - 1].xcor()
#     #     new_y = segments[seg_num - 1].ycor()
#     #     segments[seg_num].goto(new_x, new_y)
#     # segments[0].forward(20)  # finally, initial segment move to a new coordinate
#
#
#
# # tide up the code by making different classes to each task
# #tasks: create snake, move the snake,  food of the snake
#
#
# screen.exitonclick()
