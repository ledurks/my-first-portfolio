from turtle import *
import math

# Name your Turtle.
t = Turtle()
t.pencolor("white")
# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
begin_fill()
fillcolor("LightSalmon")
for sides in range(4):
    pendown()
    forward(100)
    left(90)
    penup()
end_fill()

numsides = 6

t.goto(500,300)
pendown()
for shape in range(numsides):
    forward(100)
    left(360/numsides)
    
# Close window on click.
exitonclick()
