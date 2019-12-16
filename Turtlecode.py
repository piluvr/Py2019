import turtle
import math
import random
#global variable(s)
#define global variables here
isrunning = False

def mike(t):
	isrunning = True   
	for i in range(5):
		t.color("#000000")
		t.pendown()
		t.width(3)
		t.circle(25)
		t.forward(50)
	t.right(90)
	t.forward(50)
	for i in range(5):
		draw_star(t, 20, "red")
		t.forward(50)

def draw_star(t, size, color):
	angle = 144
	t.width(3)
	l = ["#ffffff", "#f0f000", "#00ff00", "#0000ff", "#000000"]
	t.fillcolor(color)
	t.begin_fill()
	for side in range(5):
		t.speed(0)
		t.pencolor(l[side])
		t.forward(size)
		t.right(angle)
		t.forward(size)
		t.right(72 - angle)
	t.end_fill()
	return

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=700, canvheight=700, bg=None)
        print(turtle.Screen().screensize())
        w = turtle.Screen()
        t = turtle.Turtle()
        mike(t)
        w.exitonclick()
    finally:
        turtle.Terminator()
	
if __name__ == '__main__':
    main()
