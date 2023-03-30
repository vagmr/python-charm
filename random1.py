import random
import pandas as pd

# 随机生成30个人的数据
data = {'卫生满意度': [], '环境满意度': [], '服务满意度': [], '品种满意度': [], '总体满意度': []}

for i in range(30):
    hygiene = random.randint(50, 100)
    env = random.randint(50, 100)
    service = random.randint(50, 100)
    variety = random.randint(50, 100)
    overall = (hygiene + env + service + variety) / 4
    data['卫生满意度'].append(hygiene)
    data['环境满意度'].append(env)
    data['服务满意度'].append(service)
    data['品种满意度'].append(variety)
    data['总体满意度'].append(overall)

# 将数据保存为csv文件
df = pd.DataFrame(data)
df.to_csv('random2_data.csv', index=False)
