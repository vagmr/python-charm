#format
print("{0:?^30}".format("good"))
print("{0:-^50}".format(chr(10004)))
for i in range(13):
    print("{0:+^66}".format(chr(8900 + i),end =""))
print("{0:b},{0:c},{0:d},{0:o},{0:x}".format(520))
print("{0:e},{0:E},{0:f},{0:%}".format(520))
