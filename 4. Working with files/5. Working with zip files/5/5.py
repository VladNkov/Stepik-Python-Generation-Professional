from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    data_dict = {}
    for f in info:
        if not f.is_dir():
            data_dict[f.filename.split('/')[-1]] = f.date_time, f.file_size, f.compress_size

    for file_name, (data_time, file_size, compress_size) in sorted(data_dict.items()):
        print(file_name)
        print(f"  Дата модификации файла: {datetime(*data_time)}")
        print(f'  Объем исходного файла: {file_size} байт(а)')
        print(f'  Объем сжатого файла: {compress_size} байт(а)')
        print()
