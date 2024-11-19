#!/usr/bin/python3
import os
import subprocess

# Укажите путь к директории с mp4 файлами
directory = "./"

# Получаем список всех файлов в директории
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        # Полный путь к файлу mp4
        mp4_file = os.path.join(directory, filename)
        # Новое имя файла с расширением mkv
        mkv_file = os.path.join(directory, filename.rsplit('.', 1)[0] + ".mkv")

        # Команда для конвертации с помощью ffmpeg
        command = ["ffmpeg", "-i", mp4_file, "-c", "copy", mkv_file]

        # Запускаем команду
        subprocess.run(command)

        print(f"Конвертация {mp4_file} завершена.")
