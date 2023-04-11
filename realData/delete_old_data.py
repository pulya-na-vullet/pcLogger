import os
import time
import Send_to_telegramm

path = "D:/"
txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]
threshold_days = 3

for file in txt_files:
    full_file_path = os.path.join(path, file)
    if os.path.isfile(full_file_path):
        file_age = time.time() - os.path.getmtime(full_file_path)
        if file_age > threshold_days * 24 * 60 * 60:
            os.remove(full_file_path)
            Send_to_telegramm.send_message(f"File {full_file_path} has been deleted")
Send_to_telegramm.send_message("Файлы на локальном ПК не были удалены")