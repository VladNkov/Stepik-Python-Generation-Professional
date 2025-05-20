from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']


with ZipFile('test.zip', mode='a') as zip_file:
    for i in file_names:
        if os.path.exists(i) and os.path.getsize(i) <= 100:
            zip_file.write(i)