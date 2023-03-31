import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# 播放音乐文件
def play_music(file):
    subprocess.Popen(["afplay", file])

# 弹出选择框
def show_dialog():
    result = messagebox.askyesno("提示", "是否继续运行？")
    if result:
        # 如果选择“是”，关闭选择框
        root.destroy()
    else:
        # 如果选择“否”，显示图片文件
        img_file = os.path.join(os.getcwd(), "2.JPG")
        img = tk.PhotoImage(file=img_file)
        label = tk.Label(root, image=img)
        label.image = img
        label.pack()

# 创建主窗口
root = tk.Tk()
root.geometry("1200x900")

# 播放音乐文件
music_file = os.path.join(os.getcwd(), "1.MP3")
play_music(music_file)

# 显示选择框
root.after(1000, show_dialog)

# 运行主循环
root.mainloop()
