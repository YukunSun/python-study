# -*- coding: utf-8 -*-
# 文件的基本操作：按行读取
fileName = 'test.txt'
f4 = open(fileName)
for line in f4.readlines():
    print(line)
f4.close()

# seek 函数
f5 = open(fileName)
print('当前文件的指针：%s' % f5.tell())
print('当前读取的字符为：%s' % f5.read(1))
print('读取以后的指针：%s' % f5.tell())

# 利用 seek 函数修改文件的指针
f5.seek(0)
f5.seek(2, 0)  # offset=0 代表从当前位置偏移，f5.seek(2, 0)表示从当前位置偏移2个位置
# f5.seek(2,1) # 1 代表从开头偏移
# f5.seek(2,2) # 2 代表从结尾偏移
print(f5.tell())
f5.read(1)
print(f5.tell())
f5.close()