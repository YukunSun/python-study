# -*- coding: utf-8 -*-
import time

print(time.time())
print(time.localtime())

import datetime

now = datetime.datetime.now()
print(now)
delta = datetime.timedelta(days=1)
print(now + delta)

some_day = datetime.datetime(2008, 8, 25)
delta2 = datetime.timedelta(days=20, minutes=25)
print(some_day)  # 2008-08-25 00:00:00
