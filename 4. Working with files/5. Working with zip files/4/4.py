from zipfile import ZipFile

time_place = (2021, 11, 30, 14, 22, 00)
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    data_list = []

    for i in range(len(info)):
        if info[i].date_time > time_place and info[i].filename.split('/')[-1]:
            data_list.append(info[i].filename.split('/')[-1])
    print(*sorted(data_list), sep='\n')