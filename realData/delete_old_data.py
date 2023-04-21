import os
import time
import requests
import datetime
import telegram

TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
chat_id = "781078907"
bot = telegram.Bot(token=TOKEN)

# Отправка сообщения
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

# Пример использования функций
now = datetime.datetime.now()

path = "D:/"
path_log = "C:/Users/grig-/Desktop/Python_bot"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
txt_files_log = [f for f in os.listdir(path_log) if f.endswith('.txt')]
threshold_days = 0

for file in txt_files:
    full_file_path = os.path.join(path, file)
    if os.path.isfile(full_file_path):
        file_age = time.time() - os.path.getmtime(full_file_path)
        if file_age > threshold_days * 24 * 60 * 60:
            os.remove(full_file_path)
            send_message(f"Файлы на диске D {full_file_path} удален")
        else : send_message("Файлы на диске D \nПК небыли удалены")

for file in txt_files_log:
    full_file_path = os.path.join(path_log, file)
    if os.path.isfile(full_file_path):
        file_age = time.time() - os.path.getmtime(full_file_path)
        if file_age > threshold_days * 24 * 60 * 60:
            os.remove(full_file_path)
            send_message(f"Файл логов {full_file_path} удален")
        else : send_message("Файлы на локальном \nПК небыли удалены")

