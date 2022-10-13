"""unzip downloaded files
"""

import zipfile

file_zip = zipfile.ZipFile('downloaded_files/TNVED.ZIP','r')
file_zip.extractall('unzipped files/')
file_zip.close()

