#Скрипт отправки в бот сообщений о запуске
import requests
import datetime
import telegram
import os

now = datetime.datetime.now()
TOKEN = "Уникальный токен от FatherBot"
chat_id = "ИД вашего чата из скрипта first_step.py"
message = "Запуск твоего компьютера:"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={now}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
print(requests.get(url2).json())

# Устанавливаем токен бота
bot = telegram.Bot(token={TOKEN})

# Путь до файла, который нужно отправить
file_path = 'd:\Start_pc_worc.txt'

def send_file():
    # Открываем файл для чтения
    with open(file_path, 'rb') as f:
        # Отправляем файл в чат бота
        bot.send_document(chat_id='your_chat_id', document=f)

# Функция, которая проверяет, есть ли интернет-соединение
def check_internet():
    # Проверяем доступность гугл.com
    response = os.system('ping -q -c 1 google.com > /dev/null')
    if response == 0:
        return True
    else:
        return False

# Основной код
if check_internet():
    # Если есть интернет, отправляем файл
    send_file()
else:
    # Если интернет отсутствует, ждем его восстановления и отправляем файл
    while not check_internet():
        pass
    send_file()