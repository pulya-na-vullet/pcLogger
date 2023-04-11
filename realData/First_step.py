#Скрипт поиска ID чата обзения между клментом и телеграмм ботом
import requests
TOKEN = "6270028467:AAFdqmtb-gmpR4J4YQhbBZtfZ4N1SeK5VJw"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())