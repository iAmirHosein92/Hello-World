import turtle
turtle.getscreen()
turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
forward = 0

for i in range(20):
    forward += 15
    for j in range(4):
        t.fd(forward)
        t.lt(90)
    
   
