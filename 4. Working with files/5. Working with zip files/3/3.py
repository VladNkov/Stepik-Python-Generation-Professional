from zipfile import ZipFile

with ZipFile('workbook (1).zip') as zip_file:
    info = zip_file.infolist()
    file_data = {}
    for i in info:
        if not i.is_dir():
            file_data[i.filename.split('/')[-1]] = (i.compress_size/i.file_size)*100
    print(min(file_data, key=file_data.get))