import turtle
import turtle as t

mytur = t.Turtle()
screen = t.Screen()
mytur.pendown()


def moveforward():
    mytur.forward(10)

def movebackward():
    mytur.backward(10)

def turn_left():
    new_heading = mytur.heading() + 10
    mytur.setheading(new_heading)

def turn_right():
    new_heading = mytur.heading() - 10
    mytur.setheading(new_heading)

def cleanscreen():
    mytur.clear()
    mytur.penup()
    mytur.home()
    mytur.pendown()



turtle.listen()
turtle.onkey(key="w", fun=moveforward)
turtle.onkey(key="s", fun=movebackward)
turtle.onkey(key="a", fun=turn_left)
turtle.onkey(key="d", fun=turn_right)
turtle.onkey(key="c", fun=cleanscreen)


screen.exitonclick()
