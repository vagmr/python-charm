#cycle
try:
    height,weight = eval(input("请输入身高和体重的值【逗号隔开】:"))
    bmi = weight / pow(height,2)
    print("{:.2f}".format(bmi))
    who,nat= "",""
    if 18<bmi:
        who,nat ="偏瘦","偏瘦"
    elif 18<= bmi <24:
        who,nat = "正常","偏瘦"
    elif 24 <= bmi <28:
        who,nat = "偏胖","正常"
    elif 28<= bmi <30:
         who,nat = "超重","正常"
    print("国内标准为'{0}',国际标准为'{1}'".format(who,nat))
except :
    print("出错了")
else:
    print("do a good job")
finally:
    print("代码执行完毕")
