#fiboraci
def fiboraci(n):
    if n==1 or n==2:
        return 1
    else:
        return fiboraci(n-1)+fiboraci(n-2)
print("输入数值:"+"{:.2f}".format(fiboraci(12)))        
