import requests
import time
from bs4 import BeautifulSoup
import random
import json
# 本周最受欢迎
url_template = 'http://www.xiachufang.com/explore/?page={num}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
# 数据集合
data_array = []
for num in range(1, 21):
    url = url_template.format(num = num)
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    parent = bs.find('div', class_='normal-recipe-list').find_all('li')
    for item in parent:
        # 获取标题
        title = item.find('p', class_='name').find('a').text.strip()
        # 获取标题链接
        link = 'http://www.xiachufang.com' + item.find('p', class_='name').find('a')['href']
        # 获取配料
        ellipsis = item.find('p', class_='ing ellipsis').text.strip()
        # 获取七天内做过的人数
        people_num = item.find('p', class_='stats green-font').find('span', class_='bold').text
        # 获取发布该信息的作者
        author = item.find('p', class_='author').text.replace('\n', '')

        img_path = item.find('img').attrs.get('data-src')


        data_array.append({
            'title':title,
            'link':link,
            'ellipsis':ellipsis,
            'people_num':people_num,
            'img_path':img_path,
            'author':author
        })
    # time.sleep(2)
with open('test.json', 'w') as  f:
    json.dump(data_array, f)
