# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
    #"Host": "www.infoq.cn",
    #"Connection": "keep-alive",
    #"Content-Length": "39",
    "Accept": "application/json, text/plain, */*",
    #"Origin": "https://www.infoq.cn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Content-Type": "application/json",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://www.infoq.cn/hotlist?tag=day",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "_ga=GA1.2.516021722.1567219367; _itt=1; GCID=f548d1f-249e84f-50d8160-59dda84; GRID=f548d1f-249e84f-50d8160-59dda84; GCESS=BAUEAAAAAAMEvwnpXQsCBAABBJB4EAAGBIsoWmwKBAAAAAAHBFc__7IIAQMJAQECBL8J6V0MAQEEBAAvDQA-; LF_ID=1575689478221-4546442-4026981; Hm_lvt_094d2af1d9a57fd9249b3fa259428445=1575689479; _gid=GA1.2.155882405.1575689479; _gat=1; Hm_lpvt_094d2af1d9a57fd9249b3fa259428445=1575689756; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1575689766|1575689478"
}


def spider(article_url):
    response = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(response.text)
    for info in soup.find_all('div', class_='item-main'):
        print(info)


url = 'https://www.infoq.cn/hotlist?tag=day'
spider(url)
