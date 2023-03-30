import pandas as pd
import statsmodels.api as sm

# 读取数据集
data = pd.read_csv("random2_data.csv")

# 划分自变量和因变量
X = data[['卫生满意度', '环境满意度', '服务满意度', '品种满意度']]
Y = data['总体满意度']

# 添加截距项
X = sm.add_constant(X)

# 拟合多元线性回归模型
model = sm.OLS(Y, X).fit()

# 输出模型的摘要信息
print(model.summary())
