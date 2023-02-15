#常规矩形词云

#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("你的文件.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("grwordcloud.png")



#不规则图形词云

#GovRptWordCloudv2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg")
excludes = { }
f = open("你的文件.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("grwordcloudm.png")