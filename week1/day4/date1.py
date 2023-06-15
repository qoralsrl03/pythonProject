import datetime
#현재 날짜와 시간
now = datetime.datetime.now()
print(now)
#format
now_yyyymmdd = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_yyyymmdd)
now_yymmdd = now.strftime('%y-%m-%d %H:%M:%S')
print(now_yymmdd)
#문자열 to datetime
date_str = '2023-01-01 11:30:01'
format = '%Y-%m-%d %H:%M:%S'
date = datetime.datetime.strptime(date_str, format)
print(date, type(date))