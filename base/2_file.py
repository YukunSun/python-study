# -*- coding: utf-8 -*-
fileName = 'test.txt'
f1 = open(fileName, 'w')
f1.write('he')
f1.write('llo')
f1.close()

# f2 = open(fileName)
f2 = open(fileName, 'r')
print(f2.read())

# 往文件里追加(而不是覆盖)内容
f3 = open(fileName, 'a')
f3.write(' world')
f3.close()
