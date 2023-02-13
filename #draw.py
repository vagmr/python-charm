#draw
import turtle
import time
def gap():
    turtle.penup()
    turtle.fd(10)
def drawlien(draw):
    gap()
    turtle.pd() if draw else turtle.penup()
    turtle.pensize(10)
    turtle.fd(67)
    gap()
    turtle.right(90)
def drawjustify(fy):
    drawlien(True) if fy in [2,3,4,5,6,8,9] else drawlien(False)
    drawlien(True) if fy in [0,1,3,4,5,6,7,8,9] else drawlien(False)
    drawlien(True) if fy in [0,2,3,5,6,8,9] else drawlien(False)
    drawlien(True) if fy in [0,2,6,8] else drawlien(False)
    turtle.left(90)
    drawlien(True) if fy in[0,4,5,6,8,9] else drawlien(False)
    drawlien(True) if fy in[0,2,3,5,6,7,8,9] else drawlien(False)
    drawlien(True) if fy in[0,1,2,3,4,7,8,9] else drawlien(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    for i in date:
        if i == "-":
            turtle.write('年',font=("Arial",35,"normal"))
            turtle.pencolor("blue")
            turtle.fd(45)
        elif i == "=":
            turtle.write('月',font=("Arial",35,"normal"))
            turtle.pencolor("red")
            turtle.fd(45)
        elif i == "+":
            turtle.write('日',font=("Arial",35,"normal"))
            turtle.pencolor("red")
            turtle.fd(45)
        else:
            drawjustify(eval(i))
def main():
    turtle.setup(1000,660,700,700)
    turtle.penup()
    turtle.fd(-300)
    drawdate(time.strftime('%y-%m=%d+',time.gmtime()))
    turtle.hideturtle
    turtle.done()
main()
