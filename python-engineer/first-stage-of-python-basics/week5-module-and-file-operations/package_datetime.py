# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)

three_days = timedelta(days=3)
after_three_day = now + three_days
before_three_day = now - three_days
print(after_three_day)
print(before_three_day)

one_hour = timedelta(hours=1)
after_one_hour = now + one_hour
print(after_one_hour)

# 时间对象转字符串
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str)

# 时间字符串转时间类型
now_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print(now_obj)

now_timestamp = datetime.timestamp(now)
print('-----------')
print(now_timestamp)
now_datetime_obj = datetime.fromtimestamp(now_timestamp)
print(now_datetime_obj)
