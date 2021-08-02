# import colorgram
# colors = colorgram.extract('Hirst.jpg', 20)

# TODO 1 - Print the colors in jpg format
# color_list = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_pallete = (red, green, blue)
#     color_list.append(color_pallete)
# print(color_list)


# TODO 2 - Use the colors extracted from the Hirst image to create a hirst-looking painting
# Import the modules
import random
import turtle
turtle.colormode(255)
project_colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
                  (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165),
                  (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

# create turtle object-t
# Note: You wont need to use the pendown() method in this case.
# the dot() method will just leave a path along the trail
t = turtle.Turtle()
# Change the heading so that the dots start at the edge of the page
t.penup()
t.setheading(225)
t.forward(350)
t.setheading(0)
t.speed("fastest")

t.hideturtle()
total_dots = 100


for dot_count in range(1, total_dots+1):
    t.dot(15, random.choice(project_colors))
    t.forward(40)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(40)
        t.setheading(180)
        t.forward(400)
        t.setheading(0)

screen = turtle.Screen()
exit = screen.exitonclick()
