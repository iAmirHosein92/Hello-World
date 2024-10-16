import turtle
turtle.getscreen()
t = turtle.Turtle()
t.speed("fastest")
forward = 10

for i in range(20):
    t.fd(forward)
    t.lt(45)
    forward += 10
   
