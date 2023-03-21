#Скрипт отправки в бот сообщений о запуске
import requests
import datetime

now = datetime.datetime.now()
TOKEN = "Уникальный токен от FatherBot"
chat_id = "ИД вашего чата из скрипта first_step.py"
message = "Запуск твоего компьютера:"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={now}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
print(requests.get(url2).json())

file = open('Start_pc_worc_.txt','r')

