import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

root = tk.Tk()
root.withdraw()

# 让用户选择第一个csv文件的路径
file_path1 = filedialog.askopenfilename(title="选择第一个csv文件",
                                        filetypes=[("CSV Files", "*.csv")])

# 检查用户是否选择了第一个csv文件，如果没有选择则弹出提示框，让用户选择是否重新选择文件或退出程序
while not file_path1:
    response = messagebox.askquestion("提示", "您没有选择第一个csv文件，请选择是否重新选择文件或退出程序！")
    if response == "yes":
        file_path1 = filedialog.askopenfilename(title="选择第一个csv文件",
                                                filetypes=[("CSV Files", "*.csv")])
    else:
        exit()

# 让用户选择第二个csv文件的路径
file_path2 = filedialog.askopenfilename(title="选择第二个csv文件",
                                        filetypes=[("CSV Files", "*.csv")])

# 检查用户是否选择了第二个csv文件，如果没有选择则弹出提示框，让用户选择是否重新选择文件或退出程序
while not file_path2:
    response = messagebox.askquestion("提示", "您没有选择第二个csv文件，请选择是否重新选择文件或退出程序！")
    if response == "yes":
        file_path2 = filedialog.askopenfilename(title="选择第二个csv文件",
                                                filetypes=[("CSV Files", "*.csv")])
    else:
        exit()

# 读取两个csv文件，并存储为DataFrame对象
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# 将两个DataFrame对象根据列进行合并，并添加一列用于区分其来源
merged_df = pd.merge(df1, df2, how='outer', on=list(df1.columns), indicator=True)

# 根据合并后的“_merge”列将不同的部分标记为“left_only”或“right_only”
just_in_df1 = merged_df[merged_df['_merge'] == 'left_only'].drop(['_merge'], axis=1)
just_in_df2 = merged_df[merged_df['_merge'] == 'right_only'].drop(['_merge'], axis=1)

# 使用transpose方法将数据框翻转，让第一个文件放在左边，第二个文件放在右边
comparison_table = pd.concat([just_in_df1.set_index(list(df1.columns)).transpose(),
                              just_in_df2.set_index(list(df1.columns)).transpose()],
                             axis=1)

# 突出显示不同的部分
comparison_table = comparison_table.style.applymap(lambda x: 'background-color: #ffcccc', subset=(just_in_df1.index, just_in_df1.columns))\
                                       .applymap(lambda x: 'background-color: #ccffcc', subset=(just_in_df2.index, just_in_df2.columns))

# 将输出设置为自动换行
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
# 输出对比结果，并进行自动换行
print(comparison_table.to_html())