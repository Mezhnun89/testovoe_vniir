import requests
def save_from_www(link):
    filename = link.split('/')[-1]
    print(filename)
    r = requests.get(link, allow_redirects = True)
    open(filename, 'wb').write(r.content)


link = 'https://www.nalog.gov.ru/html/sites/www.new.nalog.ru/docs/sprav/tnved/TNVED.ZIP'

save_from_www(link)