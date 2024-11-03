import turtle
turtle.getscreen()
turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
turn_angle = 270
angle = 0
for i in range(270):
    angle =+ 1
    turn_around = 90 // angle
    t.rt(90)
    for j in range(turn_around):
            t.color("red")
            t.fd(200)
            t.bk(200)
            t.rt(angle)
   
