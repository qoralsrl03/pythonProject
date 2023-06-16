from get_stock import fn_stock_get
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
print('수집기 작동중!!')
def fn_interval():
    print('데이터 수집!!')
    print(datetime.datetime.now())
    fn_stock_get()
sched = BlockingScheduler()
sched.add_job(fn_interval, 'interval', minutes=10)
sched.start()