import turtle

def background(t):
	clist=["#ffffff", "#ffbfbf", "#ff6a6a", "#ff1515"]
	#w.setup(1000,700)
	for n in range(4):
		t.penup()
		t.setpos(-500,700-((n+2)*175))
		t.pendown()
		t.begin_fill()
		t.fillcolor(clist[n])
		for i in range(2):
			t.forward(1000)
			t.right(90)
			t.forward(175)
			t.right(90)
		t.end_fill()
		t.penup()
	

def main():
	w= turtle.Screen()
	t=turtle.Turtle()
	clist=["#ffffff", "#ffbfbf", "#ff6a6a", "#ff1515"]
	w.setup(1000,700)
	for n in range(4):
		t.setpos(-500,700-((n+2)*175))
		t.begin_fill()
		t.fillcolor(clist[n])
		for i in range(2):
			t.forward(1000)
			t.right(90)
			t.forward(175)
			t.right(90)
		t.end_fill()
	w.exitonclick()

if __name__ == '__main__':
	main()
