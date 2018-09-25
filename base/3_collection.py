# -*- coding: utf-8 -*-


dict = {'k1': 1, 'k2': 2, 'k3': 'k3'}
print(dict['k1'])
print(dict.get('k2'))
print(dict.pop('k2'))


s = set([1, 2, 3, 4, 5, 5])
print(s)
s.add(6)
print(s)
s.remove(5)
print(s)

s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print(s1 & s2)
print(s1 | s2)