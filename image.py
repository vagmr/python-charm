from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

# 实例化 Tkinter
root = Tk()
root.withdraw()

# 提示用户选择图片
input("请点击回车键以选择要转换的图片...")

# 弹出对话框获取输入和输出文件路径
input_file = filedialog.askopenfilename(title="选择要转换的图片", filetypes=[
    ("JPEG 文件", "*.jpg;*.jpeg;*.jfif"), 
    ("PNG 文件", "*.png"), 
    ("BMP 文件", "*.bmp"), 
    ("GIF 文件", "*.gif"), 
    ("TIFF 文件", "*.tiff;*.tif"),
    ("所有文件", "*.*")
])
output_file = filedialog.asksaveasfilename(title="保存转换后的图片", defaultextension=".png", filetypes=[("PNG 文件", "*.png"), ("所有文件", "*.*")])

# 如果输入文件不存在，打印错误消息并退出
if not os.path.exists(input_file):
    print("错误：输入文件不存在。")
    exit()

# 打开输入文件并将其转换为 PNG 格式
try:
    # 打开不同格式的图片文件并进行转换
    with Image.open(input_file) as img:
        if img.format == "PNG":
            img.save(output_file, "png")
        else:
            img.convert("RGBA").save(output_file, "png")
        print(f"图片已成功转换并保存到{output_file}")
except Exception as e:
    print("转换图片出错了：", e)
