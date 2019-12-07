# -*- coding: utf-8 -*-

# 优化正则的使用——beautiful soup
import requests
from bs4 import BeautifulSoup

url = "http://www.cnu.cc/works/288164"
html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())

# 获取 title
t = soup.title
print(t.string)
# 找到 a 标签
a = soup.a
print(a)

#

id = soup.find(id='navbar')
print(id)
