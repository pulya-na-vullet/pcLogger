import requests
import datetime
import telegram

# Установка переменных
now = datetime.datetime.now()
TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
chat_id = "781078907"
message = "Запуск твоего компьютера:"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={now}"

# Отправка сообщений в чат
print(requests.get(url).json())
print(requests.get(url2).json())
bot = telegram.Bot(token=TOKEN)
