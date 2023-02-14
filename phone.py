import turtle

# 设置画笔大小和颜色
turtle.pensize(5)
turtle.pencolor('black')

# 画手机外框
turtle.penup()
turtle.goto(-100, 200)
turtle.pendown()
turtle.goto(100, 200)
turtle.goto(100, -300)
turtle.goto(-100, -300)
turtle.goto(-100, 200)

# 画手机屏幕
turtle.penup()
turtle.goto(-80, 180)
turtle.pendown()
turtle.goto(80, 180)
turtle.goto(80, -260)
turtle.goto(-80, -260)
turtle.goto(-80, 180)

# 画手机主按钮
turtle.penup()
turtle.goto(0, -290)
turtle.pendown()
turtle.circle(30)

turtle.done()
