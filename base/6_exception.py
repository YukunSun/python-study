# -*- coding: utf-8 -*-

# 1. 异常举例
try:
    print(1 / 0)
except Exception as e:
    print('%s' % e)  # division by zero

# 2.可以包括多个指定的异常
try:
    # a = int('abc')
    v = 1 / 'a'
except (ValueError, TypeError) as e:
    print('%s' % e)

# 3.也可以自定义 异常
try:
    raise NameError('the parameter cannot be null')
except NameError as e:
    print(e)
finally:
    print('finally 最后被执行...')
