#dict
a = {}
a["亚洲"]="中国";a["大洋洲"]="澳大利亚"
a["大洋洲"]="美国";a["中国"]="印度"
if "c" in a:
    print(True)
else:
    print(False)
print(len(a))
print(a)
a.clear()
print(a)