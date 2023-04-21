import requests
import telegram
import os
import time
from datetime import datetime, timedelta

TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
CHAT_ID = "781078907"
bot = telegram.Bot(token=TOKEN)
logSavePath = 'C:/Users/grig-/Desktop/Python_bot'

# Отправка сообщения
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)
#Создание файла скриптом python
def record_auth_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    filename = "Start_pc_work_" + time.strftime("%Y_%m_%d_%H_%M_%S") + ".txt"
    with open(filename, "w") as f:
        print("Файл скриптом python создан")
        f.write("User authorized at: " + current_time)
    return filename
#Чтение последней строки в последнем созданном файле
def read_last_line_from_latest_file(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        return None

    latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(directory, x)))
    latest_file_path = os.path.join(directory, latest_file)

    if not os.path.isfile(latest_file_path):
        return None

    with open(latest_file_path) as f:
        lines = f.readlines()

    if not lines:
        return None

    return lines[-1].strip()
#Запись старта работы в день для расчета времени работы.
def record_start_work_time_in_day():
    startWorkDataTime = time.strftime("%d%m%Y %H:%M")
    workLogFilename = "workTimeDataSave.txt"
    with open(workLogFilename, "a") as f:
        f.write("\n" + startWorkDataTime)
    return startWorkDataTime
#Проверки рабочего времени

# Основнеое тело:
record_auth_time()
record_start_work_time_in_day() 
latest_line = read_last_line_from_latest_file(logSavePath)
send_message("Запуск твоего компьютера: " + time.strftime("\nДата: %Y-%m-%d \nВремя: %H:%M"))
print("Сообщение о запуске отправленно в телеграмм " + time.strftime("%Y-%m-%d %H:%M:%S"))

latest_line = read_last_line_from_latest_file(logSavePath)
if latest_line:
    print("Строка в файле Start_pc_work: " + latest_line)
else:
    #Аллертер об ошибках.
    send_message("Что то пошло не так при записи файлов")

#Анализатор рабочего кол-ва проведенного рабочего времени
def analyze_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Получаем первую дату и время
    date_id, start_work_data_time = lines[0].split()
    start_work_data_time = datetime.strptime(start_work_data_time, '%H:%M')
    
    # Ищем последнюю дату и время
    for line in reversed(lines):
        if line.startswith(date_id):
            _, end_work_data_time = line.split()
            end_work_data_time = datetime.strptime(end_work_data_time, '%H:%M')
            break
    #Записываем даные входа в систему в f строки в переменную    
    start_and_stop_work_time_f_string = f"Время работы больше 8 часов можно идти домой\nПервая авторизация:       {start_work_data_time}\nПоследняя авторизация: {end_work_data_time}"
    # Считаем разницу между временами
    work_time = end_work_data_time - start_work_data_time

    # Сравниваем с 8 часами
    if work_time > timedelta(hours=8):
        send_message(start_and_stop_work_time_f_string)
    else:
        send_message(f'Ты проработал: {work_time.total_seconds() / 3600:.1f} часа(ов)\nНужно еще доработать\nСБ бдит!')
analyze_file('workTimeDataSave.txt')