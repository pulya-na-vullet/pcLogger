import os
import time
import requests
import datetime
import telegram

TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
chat_id = "781078907"
bot = telegram.Bot(token=TOKEN)

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

path = "D:/"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
threshold_days = 3

for file in txt_files:
    full_file_path = os.path.join(path, file)
    if os.path.isfile(full_file_path):
        file_age = time.time() - os.path.getmtime(full_file_path)
        if file_age > threshold_days * 24 * 60 * 60:
            os.remove(full_file_path)
            print(f"File {full_file_path} has been deleted")
    else:
       print('Nothing to delete')


# Пример использования функций
now = datetime.datetime.now()
send_message("Были уалены старые файлы")