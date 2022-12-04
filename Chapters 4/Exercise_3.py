import math
import turtle

def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r * 2 + 10)
    t.pd()

def polypie(t, n, r):
    angle = 360 / n
    for i in range(n):
        isosoceles(t, r, angle/2)
        t.lt(angle)

def isosoceles(t, r, angle):
     y = r * math.sin(angle * math.pi / 180)

     t.rt(angle)
     t.fd(r)
     t.lt(90+angle)
     t.fd(2*y)
     t.lt(90+angle)
     t.fd(r)
     t.lt(180-angle)

t = turtle.Turtle()

t.pu()
t.bk(90)
t.pd()

size = 40
draw_pie(t, 5, size)
draw_pie(t, 6, size)
draw_pie(t, 7, size)

t.hideturtle()
turtle.mainloop()
