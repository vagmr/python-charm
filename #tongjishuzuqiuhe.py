#tongjishuzuqiuhe
num = []
def getnum():
    global num
    innum = input("请输入数字:")
    while innum != "":
        num.append(eval(innum))
        innum = input("请输入数字:")
    return num
def sum(num):
    sum = 0.0
    for n in num:
        sum += n
    return sum/len(num)
def variance(num,sum):
    var = 0
    for i in num:
        var += (i - sum)**2
    suvar = pow((1/len(num))*var,0.5)
    return suvar
def midrian(num):
    sorted(num)
    size = len(num)
    if size % 2 == 0:
        mid = (num[size//2-1]+num[size//2])/2
    else:
        mid = num[size//2]
    return mid
b = 0
num = getnum()
b = sum(num)
print("这组数的平均值:{}方差:{}中位数:{}".format(b,variance(num,b),midrian(num)))
