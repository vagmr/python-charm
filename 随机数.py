#random
import random
import time
a = 1
b = time.perf_counter()
while  a <= 10:
    a = a + 1
    print("\n输出随机数(保留三位小数）：" + "{:.3f}".format(random.random()))
    time.sleep(0.1)
    print("\n输出整数随机数：" + "{:-^10}".format(random.randint(10,520)))
    time.sleep(0.1)
    print(time.perf_counter() - b)
print("{:-^56}".format("分割线"))
while a <= 25:
    a = a + 2
    print("\n输出范围随机数:" +str(random.randrange(25,1000,6)))
    time.sleep(0.2)
    print("\n输出比特随机数:" + "{:.0f}".format(random.getrandbits(19)))
    time.sleep(0.2)
    print(time.perf_counter() - b)
print("这又是一条分割线".center(60,"="))
while a<= 55:
    a = a + 3
    print("\n生产a到b之间的随机数：" + "{:.3f}".format(random.uniform(a,255)))
    time.sleep(0.3)
for i in range(100):
    print("\n输出0到99的数" + str(i))
    print("\n输出0到100列表中的随机数:" + str(random.choice(range(0,100))))
    time.sleep(0.3)
print("{:=^66}".format("有一条分割线"))
s = [1,2,3,4,5,6,6,7,7,8,9,10]
print("输出逆序数；" +str(s[::-1]))
random.shuffle(s);print(s)
print(time.perf_counter() - b)
print("程序运行结束")
pi = 0
n = eval(input("请输入n的值:"))
for k in range(n):
    pi += 1/pow(16,k) * (4/(8*k + 1)) - \
        2/(8*k+4) - 1/(8*k+5)-\
        1/(8*k+6)
    print("\n输出圆周率的值：{:.65f}".format(pi))
