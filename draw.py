#绘图
import turtle
def koch(size,n):
	if n == 0:
		turtle.fd(size)
	else:
		for angle in [0,90,270,-45]:
			turtle.left(angle)
			koch(size/2,n-1)
def main(v):
		turtle.screensize(1200,1200,"black")
		turtle.speed(30)
		turtle.pensize(3)
		turtle.pencolor("red")
		turtle.penup()
		turtle.goto(90,0)
		turtle.pd()
		koch(700,v)
		turtle.pencolor("green")
		turtle.penup()
		turtle.goto(180,30)
		turtle.pd()
		turtle.left(270)
		koch(700,v)
		turtle.pencolor("white")
		turtle.left(90)
		koch(700,v)
		turtle.hideturtle()
		turtle.done()
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
print(main(5))
print(cuasul(6))