import turtle

# 设置画布大小
turtle.setup(800, 600)

# 画笔设置
turtle.pensize(2)
turtle.pencolor('black')

# 绘制电脑屏幕
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.fillcolor('black')
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

# 显示画布
turtle.done()