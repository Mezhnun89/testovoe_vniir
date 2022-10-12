import zipfile

file_zip = zipfile.ZipFile('TNVED.ZIP','r')
file_zip.extractall('./')
file_zip.close()

