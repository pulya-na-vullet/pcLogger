#Скрипт поиска ID чата обзения между клментом и телеграмм ботом
import requests
TOKEN = "Уникальный токен от FatherBot"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())