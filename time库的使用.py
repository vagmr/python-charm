#time
import time
print(time.time())
print(time.ctime())
print(time.gmtime())
t = time.gmtime()
print(time.strftime("%Y-%m-%B-%b-%d-%A-%a-%H-%I-%p-%M-%S",t))
a = '2021-10-4 14:13:43'
print(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
