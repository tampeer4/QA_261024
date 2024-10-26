# TIME

# import time

# epoch_seconds = time.time()
# print("Секунды с эпохи:", epoch_seconds)


# import time

# print("Ожидание 3 секунды...")
# time.sleep(3)  
# print("Продолжение выполнения")


# import time

# text = "Загрузка данных: "
# for char in text:
#     print(char, end='', flush=True)
#     time.sleep(0.1)  

# print("Завершено!")

# import time

# start_time = time.time()
# print(start_time)
# sum_ = sum(range(50000000))
# end_time = time.time()
# print("Время выполнения:", end_time - start_time, "секунд")

# --------------------------------------------------------------------------

# DATETIME

# from datetime import datetime
# now = datetime.now()
# print(now)

# from datetime import datetime
# utc_datetime = datetime.utcnow()
# print(utc_datetime)

# from datetime import datetime
# date_string = "2023-10-23 12:45:00"
# date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S') # parse
# print(date_object)

# from datetime import datetime
# now = datetime.now()
# formatted_string = now.strftime('%Y-%m-%d %H:%M:%S') # format
# print(now)

# date_iso_string = "2025-10-28T12:45:00"
# date_object_iso = datetime.fromisoformat(date_iso_string)
# print(date_object_iso)


# from datetime import date

# today = date.today()
# print(today)


# from datetime import date
# today = date.today()
# formatted_date = today.strftime('%d/%m/%Y')
# print(formatted_date)


# now = datetime.now()
# print(now)
# current_time = now.time()
# print(current_time)


# from datetime import time

# t = time(14, 30, 45)
# print(t)
# print("Часы:", t.hour)
# print("Минуты:", t.minute)
# print("Секунды:", t.second)

# from datetime import time
# t = time(14, 30, 45)
# formatted_time = t.strftime('%H:%M:%S')
# print(formatted_time)


# from datetime import timedelta

# delta = timedelta(days=5, hours=3)
# print(delta)

# import datetime

# dt = datetime.datetime(2023, 10, 26, 14, 30)
# print("Datetime:", dt)
# print("Datetime:", type(dt))

# print("Часть даты:", dt.date())
# print("Часть времени:", dt.time())
# print(datetime.datetime.now().date())
# print("День:", dt.day)

# one_week = datetime.timedelta(weeks=1)
# next_week = dt + one_week
# print("След. неделя:", next_week)

# t1 = datetime.datetime(2023, 10, 1)
# t2 = datetime.datetime(2023, 10, 5)
# delta = t2 - t1
# print(type(delta))
# print(dir(delta))


# from datetime import datetime, date, timedelta

# d1 = date(2025, 10, 26)
# print(d1)
# d2 = date(2023, 9, 15)
# print(d2)

# d3 = d1 - d2
# print(d3)



from datetime import datetime, timedelta

# Начальная дата проекта
project_start_date = datetime(year=2025, month=10, day=23)

# Этапы проекта (в днях)
phase_one_duration = timedelta(days=10)
phase_two_duration = timedelta(days=20)
phase_three_duration = timedelta(days=15)

phase_one_end = project_start_date + phase_one_duration
# print(phase_one_end)
phase_two_start = phase_one_end
phase_two_end = phase_two_start + phase_two_duration

phase_three_start = phase_two_end
phase_three_end = phase_three_start + phase_three_duration


print(f"Начало проекта: {project_start_date.strftime('%Y-%m-%d')}")
print(f"Конец первого этапа: {phase_one_end.strftime('%Y-%m-%d')}")
print(f"Начало второго этапа: {phase_two_start.strftime('%Y-%m-%d')}")
print(f"Конец второго этапа: {phase_two_end.strftime('%Y-%m-%d')}")
print(f"Начало третьего этапа: {phase_three_start.strftime('%Y-%m-%d')}")
print(f"Конец третьего этапа: {phase_three_end.strftime('%Y-%m-%d')}")


current_date = datetime.now()

time_since_start = current_date - project_start_date
print(f"Прошло с начала проекта: {time_since_start.days} дней")

if current_date >= phase_three_end:
    print("Проект завершён.")
else:
    time_to_end = phase_three_end - current_date
    print(f"До завершения проекта осталось: {time_to_end.days} дней")