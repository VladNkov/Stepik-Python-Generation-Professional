from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    print(f'Объем исходных файлов: {sum(i.file_size for i in info)} байт(а)')
    print(f'Объем сжатых файлов: {sum(i.compress_size for i in info)} байт(а)')