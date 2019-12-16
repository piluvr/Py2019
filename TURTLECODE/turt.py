import turtle
import Star 
import bg
import Jimmy
def main():
	n= int(input("How many stars do you want on your Dragon Ball? (enter a number from 1-7)"))
	t = turtle.Turtle()
	w = turtle.Screen()
	w.setup(1000,700)
	t.hideturtle()
	t.speed(10)
	bg.background(t)
	Jimmy.dball(t)
	Star.stars(t, 65,"red", n)
	w.exitonclick()
	

if __name__ == '__main__':
	main()
