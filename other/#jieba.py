#jieba
import jieba
print(jieba.lcut("我觉得你就是个傻子"))
print(jieba.lcut("我觉得你就是个傻子",cut_all=True))
print(jieba.lcut_for_search("我觉得你就是个傻子"))
