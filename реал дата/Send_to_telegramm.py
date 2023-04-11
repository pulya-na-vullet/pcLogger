import requests
import datetime

now = datetime.datetime.now()
TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
chat_id = "781078907"
message = "Запуск твоего компьютера:"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={now}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
print(requests.get(url2).json())

file = open('Start_pc_worc_.txt','r')

