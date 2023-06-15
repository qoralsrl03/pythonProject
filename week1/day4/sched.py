#pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
def fn_interval():
    print('interval')
    print(datetime.datetime.now())
def fn_cron():
    print('cron')
    print(datetime.datetime.now())
sched = BlockingScheduler()
# 잡 등록
# 10초마다 호출
sched.add_job(fn_interval,'interval',seconds=10)
# 매일 16시 30분
# day_of_week='mon' <-- 월요일만
# day = '1' <-- 매월 1일만
# month='1, day='1' <-- 매년 1월 1일
sched.add_job(fn_cron, 'cron', hour='16', minute='30')
sched.start()