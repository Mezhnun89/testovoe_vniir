import requests


zip_url = 'https://www.nalog.gov.ru/html/sites/www.new.nalog.ru/docs/sprav/tnved/TNVED.ZIP'

def download_zip(url = ''):
    
    try:
        response = requests.get(url = url)
        
        with open('extract_files/TNVED.ZIP', 'wb') as file:
            file.write(response.content)
            
        return 'file successfully downloaded!'

    except Exception as ex:
        return 'Upps'
    

def main():
    print(download_zip(url = zip_url))
    

if __name__ == '__main__':
    main()