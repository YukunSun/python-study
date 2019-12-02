# -*- coding: utf-8 -*-
# 上下文管理器

# 读取文件，释放
fd = open('test.txt')
try:
    for line in fd:
        print(line)
finally:
    fd.close()

# 使用 with:无论有没有异常，都会释放
with open('test.txt') as f:
    for line in f:
        print(line)
