#pregressq3
import time
width = 50
print("执行开始".center(width//2,"-"))
start = time.perf_counter()
for i in range(width + 1):
	a = "» "* i
	b ="/ "* (width - i)
	c = (i/width) * 100
	d = time.perf_counter() - start
	print("\r{:^4.0f}%[{}->{}]{:.2f}s".format(c,a,b,d),end = "")
	time.sleep(0.2)
print("\n "+"执行结束:伞兵"[::-1].center(width//2,"-"))

      
    
