from datetime import datetime, timedelta

# 1)
print(datetime.now())
print(datetime.now() - timedelta(days=5))

print("-" * 30)

# 2)
print("yesterday: ", datetime.now() - timedelta(days=1))
print("today: ", datetime.now())
print("tomorrow: ", datetime.now() + timedelta(days=1))

print("-" * 30)

# 3)
print("datetime without microseconds")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("-" * 30)

# 4)
date1 = datetime.now()
date2 = datetime(2021, 6, 1, 23, 30, 30)
difference = date1 - date2
print(difference.total_seconds())


