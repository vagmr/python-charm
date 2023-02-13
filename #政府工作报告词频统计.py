#政府工作报告词频统计
import jieba
def gettxt():
    txt = open("2.txt","r",encoding='utf-8').read()
    jieba.lcut(txt)
    return txt
word = gettxt()
words = word.split()
dict = {}
for i in words:
    dict[i]=dict.get(i,0)+1
zflist = list(dict.items())
zflist.sort(key=lambda x:x[1],reverse=True)
for a in range(1):
    b,c=zflist[a]
print("出现的词为{0:^5}出现的次数为{1:<12}".format(b,c))