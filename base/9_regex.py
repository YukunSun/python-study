# -*- coding: utf-8 -*-
import re

p = re.compile('.{3}')
print(p.match('cataa'))

print(re.compile(r'(\d+)-(\d+)-(\d+)').match('2019-08-11'))  # <re.Match object; span=(0, 10), match='2019-08-11'>
print(re.compile(r'(\d+)-(\d+)-(\d+)').match('2019-08-11').group())  # 2019-08-11
print(re.compile(r'(\d+)-(\d+)-(\d+)').match('2019-08-11').groups())  # ('2019', '08', '11')
print(re.compile(r'(\d+)-(\d+)-(\d+)').findall('2019-08-11 hello 2019-02-21'))  # [('2019', '08', '11'), ('2019', '02', '21')]

print(re.sub(r'\D', '', '12-3-4-5-6 #hello world'))  # 123456
