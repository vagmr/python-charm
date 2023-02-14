import turtle

# 设置画布大小
turtle.setup(800, 600)

# 画笔设置
turtle.pensize(2)

# 绘制电脑屏幕
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.fillcolor('#8FAADC')
turtle.begin_fill()
turtle.goto(300, 200)
turtle.goto(300, -200)
turtle.goto(-300, -200)
turtle.goto(-300, 200)
turtle.end_fill()

# 绘制电脑边框
turtle.penup()
turtle.goto(-320, 220)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.goto(320, 220)
turtle.goto(320, -220)
turtle.goto(-320, -220)
turtle.goto(-320, 220)
turtle.end_fill()

# 绘制桌面
turtle.penup()
turtle.goto(-400, -250)
turtle.pendown()
turtle.fillcolor('#CA9C70')
turtle.begin_fill()
turtle.goto(400, -250)
turtle.goto(400, -300)
turtle.goto(-400, -300)
turtle.goto(-400, -250)
turtle.end_fill()

# 显示画布
turtle.done()