# основной файл для проекта hello-world-semver
import datetime

print("Hello world!") # В этой строке выводится приветствие

# Новая функция: печать текущей даты и времени
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Время: {current_time}.") # Исправлено форматирование и добавлена точка
