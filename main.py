# основной файл для проекта hello-world-semver
import datetime

user_name = "Angelina"# Новая переменная для имени пользователя
print(f"Hello + {user_name}!") #  Обновлено приветствие

# Новая функция: печать текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time is: {current_time}.") # Исправлено форматирование и добавлена точка
