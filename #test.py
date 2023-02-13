#test
import jieba
a = open("三国演义.txt","rt",encoding="utf-8").read()
print(jieba.lcut(a))
