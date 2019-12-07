# -*- coding: utf-8 -*-
import requests
import re
import os
import shutil

# 抓取图片

url = 'http://www.cnu.cc/inspirationPage/recent-226'
content = requests.get(url).text
# <img src="http://img.cnu.cc/uploads/images/flow/1909/12/eb682b96fefa372bae04c816d5547cd7.jpg?width=1000&amp;height=667" alt="美丽大自然 | Zack Seckler航拍作品">
pattern = re.compile(r'<img src="(.*?)" alt="(.*?)">')
results = re.findall(pattern, content)

for result in results:
    print(result[0], result[1])
    # 下载图片
    img_url = result[0]
    response = requests.get(img_url, stream=True)
    dir = os.path.abspath('.')
    img_path = os.path.join(dir, result[1] + '.jpg')
    if response.status_code == 200:
        with open(img_path, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)
