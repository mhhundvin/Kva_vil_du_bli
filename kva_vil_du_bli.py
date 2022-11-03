import turtle
import random

tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

tim.shape("turtle")
tim.color("red")



shapes = ["circle", "turtle", "triangle", "classic"]
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']


##################################################################################################
def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

def click_left(x, y):
    tim.color(random.choice(colors))

def click_right(x, y):
    tim.stamp()

def shape_turtle():
    tim.shape(random.choice(shapes))
    # tim.shape('turtle')


turtle.listen()

turtle.onscreenclick(click_left, 1)
turtle.onscreenclick(click_right, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.onkey(shape_turtle, 'space')

turtle.mainloop()

