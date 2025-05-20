from zipfile import ZipFile
import os.path

# with ZipFile('test.zip') as zip_file:
size = os.path.getsize('test.zip')
print(size)
