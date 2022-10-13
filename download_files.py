"""download_files

    Returns:
        _type_: function for downloading files
    """

import requests
from pathlib import Path


zip_url = 'https://www.nalog.gov.ru/html/sites/www.new.nalog.ru/docs/sprav/tnved/TNVED.ZIP'
current_directory = Path(__file__).parent.absolute()

def download_zip(url = ''):
    
    try:
        response = requests.get(url = url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        print (response.status_code)
        data_path = current_directory / 'downloaded_files/TNVED.ZIP'
        print(data_path)
        with open(data_path, 'wb') as file:
            file.write(response.content)
            
        return 'file successfully downloaded!'

    except Exception as ex:
        return 'Upps... Check the URL please!'
    

def main():
    print(download_zip(url = zip_url))
    

if __name__ == '__main__':
    main()