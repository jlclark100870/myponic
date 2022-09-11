from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import sys


def download_and_unzip(url, extract_to='../myponic'):
    try:
        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=extract_to)
    except:
    
        print( sys.exc_info()[1])
        print('Exception occured', exc_info=True)
        
download_and_unzip('https://github.com/jlclark100870/csskp-ponics/archive/refs/heads/main.zip')