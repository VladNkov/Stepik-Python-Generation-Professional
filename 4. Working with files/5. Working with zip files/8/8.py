from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name, 'r') as zip_file:
        if len(args) == 0:
            zip_file.extractall()
        else:
            for i in args:
                zip_file.extract(i)


extract_this('workbook.zip', 'earth.jpg', 'exam.txt')