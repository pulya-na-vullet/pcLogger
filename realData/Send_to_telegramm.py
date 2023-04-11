import requests
import datetime
import telegram
import os
from datetime import date

now = datetime.datetime.now()
TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
chat_id = "781078907"
message = "Запуск твоего компьютера:"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={now}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
print(requests.get(url2).json())

bot = telegram.Bot(token=TOKEN)

def send_files(files):
    for file in files:
        with open(file, 'rb') as f:
            bot.send_document(chat_id=chat_id, document=f)

def get_today_files():
    today = date.today()
    folder = 'D:/'
    files = os.listdir(folder)
    today_files = []
    for file in files:
        if os.path.isfile(os.path.join(folder, file)) and file.endswith('.txt') and file.startswith('Start_pc_worc_'):
            today_files.append(os.path.join(folder, file))
    return today_files

if __name__ == '__main__':
    files = get_today_files()
    send_files(files)