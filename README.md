# python-charm
Python
Python是一种高级编程语言，最初由Guido van Rossum于1991年开发，现在由Python软件基金会维护。Python具有简洁易读的语法、动态类型、垃圾回收、强大的标准库和丰富的第三方库，被广泛应用于Web开发、科学计算、人工智能、数据分析等领域。

安装Python
在开始Python编程之前，需要先安装Python。Python可以从官方网站python.org上下载，也可以使用包管理器（如apt、yum、brew等）在命令行中安装。

安装Python后，可以在命令行中输入python命令来进入Python交互模式，或者使用文本编辑器编写Python脚本并执行。

基本语法
变量
在Python中，变量是动态类型的，可以随时改变其类型和值。定义变量时不需要指定类型，Python会自动推断。

python
Copy code
x = 1
y = 2.0
z = "hello"
数据类型
Python支持多种内置数据类型，包括整数、浮点数、布尔值、字符串、列表、元组、字典等。这些数据类型可以进行各种操作，如算术运算、比较运算、逻辑运算、索引、切片等。

python
Copy code
a = 1 + 2     # 整数加法
b = 3.14 - 1  # 浮点数减法
c = True and False  # 逻辑与
d = "hello" + "world"  # 字符串拼接
e = [1, 2, 3]  # 列表
f = (4, 5, 6)  # 元组
g = {"name": "Tom", "age": 20}  # 字典
条件语句
Python中的条件语句可以使用if、elif、else关键字来实现。条件语句根据条件表达式的值来决定执行哪个分支。

python
Copy code
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
循环语句
Python中的循环语句可以使用for、while关键字来实现。for循环可以遍历列表、元组、字典等可迭代对象；while循环可以在满足条件的情况下重复执行一段代码块。

python
Copy code
# for循环遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while循环计算斐波那契数列
a, b = 0, 1
while b < 100:
