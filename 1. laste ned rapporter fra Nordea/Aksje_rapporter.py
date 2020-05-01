import urllib.request
import datetime


def download_rapports(url):
    name = datetime.datetime.today()
    full_name = str(name)
    urllib.request.urlretrieve(url, full_name)
    
download_rapports(str(input()))




    