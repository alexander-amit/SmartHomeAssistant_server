 
    
import requests
from requests.auth import HTTPDigestAuth
import json

def takeImage():
    
    url = "http://localhost:9000/take_image"
    print('method before called')
    myResponse = requests.get(url)
    print('method called')
    if(myResponse.ok):
        print('method status is ok')
        return myResponse.content
    else:
        print('error occured')
        myResponse.raise_for_status()
        return 'error occured'