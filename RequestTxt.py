import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 设置要爬取的小说网站的首页链接
url = ' '

# 发送请求，获取页面内容
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'   # 确定编码方式
html = response.text

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(html, 'html.parser')

# 找到小说列表
novel_list = soup.find_all('div', class_='novel-list')

# 遍历小说列表，获取小说详情页链接
for novel in novel_list:
    novel_url = novel.find('a')['href']
    # 发送请求，获取小说详情页内容
    novel_response = requests.get(novel_url, headers=headers)
    novel_response.encoding = 'utf-8'
    novel_html = novel_response.text
    # 使用BeautifulSoup解析小说详情页内容
    novel_soup = BeautifulSoup(novel_html, 'html.parser')
    # 找到小说正文部分
    novel_content = novel_soup.find('div', class_='novel-content')
    # 将小说正文保存到文件中
    with open('novel.txt', 'a', encoding='utf-8') as f:
        f.write(novel_content.get_text())
