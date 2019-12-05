# -*- coding: utf-8 -*-
import os

# 当前目录所在的绝对路径位置
print(os.path.abspath('.'))
print(os.path.exists('/Users'))
print(os.path.join('/Users', 'a', 'b'))  # /Users/a/b
print(os.path.isdir('/Users'))  # True

from pathlib import Path

# 相对于当前位置，创建目录
new_path = Path('tmp/a/b')
# parents = True 表示如果上一级目录不存在，则创建
Path.mkdir(new_path, parents=True)
