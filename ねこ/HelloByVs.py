from datetime import datetime, timedelta, timezone

now = datetime.now()
beijing_time = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8)))


print("年:", now.year)
print("月:", now.month)
print("日:", now.day)
print("北京时间:", beijing_time.strftime("%Y-%m-%d %H:%M:%S"))