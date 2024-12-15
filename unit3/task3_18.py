from datetime import datetime, timedelta

N = int(input('дней='))

# получаем текущую дату
time_now = datetime.now()

# рассчитываем дату через N дней
print(time_now + timedelta(days=N))