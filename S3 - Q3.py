import turtle
turtle.getscreen()
t = turtle.Turtle()
t.speed("fastest")
turn_angle = 270
angle = 0

for i in range(270):
    angle =+ 1
    turn_around = 270 // angle
    t.lt(270)
    for j in range(turn_around):
            t.fd(200)
            t.bk(200)
            t.rt(angle)
   
