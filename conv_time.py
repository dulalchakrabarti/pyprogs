from datetime import datetime
date_time_str = '2022-03-30 00:45:00.000Z'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%fZ')
tm = datetime.timestamp(date_time_obj)
print(tm)

