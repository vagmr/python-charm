import turtle

# 设置画笔大小和颜色
turtle.pensize(3)
turtle.pencolor('black')

# 绘制少女头部
turtle.penup()
turtle.goto(-40, 80)
turtle.pendown()
turtle.circle(40)

# 绘制少女头发
turtle.penup()
turtle.goto(-80, 80)
turtle.pendown()
turtle.right(30)
turtle.circle(80, 60)
turtle.right(120)
turtle.circle(80, 60)
turtle.right(150)
turtle.circle(80, 60)

# 绘制少女眼睛
turtle.penup()
turtle.goto(-20, 100)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(20, 100)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# 绘制少女嘴巴
turtle.penup()
turtle.goto(-20, 70)
turtle.pendown()
turtle.right(90)
turtle.circle(20, 180)

# 绘制少女身体
turtle.penup()
turtle.goto(-40, 0)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# 绘制少女裙子
turtle.penup()
turtle.goto(-80, -40)
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.end_fill()

#绘制少女左手
turtle.penup()
turtle.goto(-80, 20)
turtle.pendown()
turtle.right(90)
turtle.circle(30, 180)

#绘制少女右手
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.circle(30, 180)

#绘制少女左脚
turtle.penup()
turtle.goto(-60, -70)
turtle.pendown()
turtle.right(30)
turtle.forward(60)
turtle.right(150)
turtle.forward(60)

#绘制少女右脚
turtle.penup()
turtle.goto(20, -70)
turtle.pendown()
turtle.right(30)
turtle.forward(60)
turtle.right(150)
turtle.forward(60)

turtle.done()