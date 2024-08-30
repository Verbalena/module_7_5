# Файлы в операционной системе
import os
import time

directory = '.' # обходим директорию

for root, dirs, files in os.walk(directory):
    for file in files:
        # формируем полный путь к файлу
        file_path = os.path.join(root, file)
        # получение времени последнего изменения файла
        file_time = os.path.getmtime(file_path)
        # формируем время для удобного отображения
        format_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        # получаем размер файла
        file_size = os.path.getsize(file_path)
        # получаем родительскую директорию файла
        dir_parent = os.path.dirname(file_path)
        print(f'Обнаружен файл {file}, путь: {file_path}, размер: {file_size} байт, время изменения {format_time}, родительская директория: {dir_parent}')



