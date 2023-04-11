@echo off
@echo Vremya vhoda v kompucter %date% %time% >> d:\Start_pc_worc_%date%.txt

timeout 30
python D:\Send_to_telegramm.py %*
temeout 2
python D:\delete_old_data.py %*
