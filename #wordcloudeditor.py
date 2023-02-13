#wordcloudeditor
import jieba
import wordcloud
t = open("政府工作报告.txt",'r',encoding='utf-8')
m = t.read()
t.close()
ls = jieba.lcut(m)
txt = " ".join(ls)
w = wordcloud.WordCloud ( font_path = "msyh.ttf" ,width=1920 ,height=1080,\
        background_color = 'yellow')
w.generate(txt)
w.to_file("ceshi.png")