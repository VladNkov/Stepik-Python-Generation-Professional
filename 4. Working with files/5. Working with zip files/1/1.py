from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    print(sum(1 for i in zip_file.infolist() if not i.is_dir()))
