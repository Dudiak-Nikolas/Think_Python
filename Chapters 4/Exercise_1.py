import math
import turtle

t = turtle.Turtle()

def circle(t, r):
    arc(t, r, 360)

   
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

        
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
   
if __name__ == '__main__':
    
    radius = 100
    t.pu()
    t.fd(radius)
    t.lt(90)
    t.pd()
    circle(t, radius)
  
turtle.mainloop()


