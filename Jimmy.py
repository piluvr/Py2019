import turtle 
def dball(t):
	t.color("#000000")
	t.fillcolor("#fc9003")
	t.penup()
	t.setpos(0,-250)
	t.begin_fill()
	t.color("#fc9003")
	t.circle(250)
	t.end_fill()
	t.color("#000000")
	t.pendown()
	t.width(3)
	t.circle(250)
	t.penup()
	t.setpos(-25,0)
	
def main():
	n=1
	clist = ["#000000", "#150c00", "#2a1801", "#3f2401", "#543001", "#693c01", "#7e4802", "#935402", "#a86002", "#bd6c02", "#d27802", "#e78403", "#fc9003", "#fc9003", "#fc9003"]
	t=turtle.Turtle()
	w=turtle.Screen()
	w.setup(1000,700)
	dball(t)
	t.setpos(0,0)
	t.pendown()
	for n in range(150):
		t.forward(n)
		t.left(36)
		if(n != 0):
			t.color(clist[int(n/10)])
	w.exitonclick()

if __name__ == '__main__':
	main()
