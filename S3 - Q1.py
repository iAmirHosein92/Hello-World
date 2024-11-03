import turtle
turtle.getscreen()
t = turtle.Turtle()
t.speed("fastest")
forward = 70

for i in range(24):
    t.fd(forward)
    t.lt(90)
    forward += 20
