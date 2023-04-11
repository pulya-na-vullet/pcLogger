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
send_message("Запуск твоего компьютера:")
send_message(now)