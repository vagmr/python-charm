import turtle
def koch(size,n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3,n-1)
def main():
	turtle.screensize(800,800,"black")
	turtle.speed(8)
	turtle.pensize(4)
	turtle.pencolor("red")
	turtle.penup()
	turtle.goto(60,120)
	turtle.pd()
	level = 3
	koch(400,level)
	turtle.left(120)
	koch(400,level)
	turtle.left(120)
	koch(400,level)
	turtle.hideturtle()
	turtle.reset()
def cycle():
	for h in range(1,40):
		if h < 8:
			turtle.speed(8)
			turtle.pencolor("blue")
			turtle.seth(0)
			turtle.left(135)
			turtle.fd(30)
			turtle.left(90)
			turtle.fd(30)
			turtle.right(150)
			turtle.fd(30)
		else:
			turtle.speed(9)
			turtle.pencolor("orange")
			turtle.circle(150,60)
			turtle.left(150)
			turtle.circle(100,75)
def cuasul(c):
		turtle.screensize(900,900,"black")
		turtle.penup()
		turtle.goto(60,50)
		turtle.pd()
		turtle.pencolor("white")
		if c == 1:
			cycle()
		else:
			turtle.fd(100)
			turtle.left(90)
			cycle()
			c -= 1
print(main())
print(cuasul(6))