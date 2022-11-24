from zipfile import ZipFile

with ZipFile('example.zip', 'w') as zp:
    zp.write('dane.txt')
    # zp.write('content2.txt')
    # zp.write('subfolder/content3.txt')
    # zp.write('subfolder/content4.txt')

with ZipFile('example.zip') as zp:
    zp.extract('dane.txt', 'extract_zip')
    # zp.extract('subfolder/content3.txt', 'extract_zip')
