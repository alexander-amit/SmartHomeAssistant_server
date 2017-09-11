from flask import Flask
from flask import render_template
from speak import takeOrder

import reply
import takeImage
import detectImage
import requests
from detectImage import run_inference_on_image
import base64
from tensorflow.contrib.framework.python.ops import variables
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pyttsx3
from pyttsx3 import engine

app = Flask(__name__)

@app.route('/')
def index():
   
    return render_template('index.html')


@app.route('/give_order')
def give_order():
    orderGiven = takeOrder()
    retMsg = recognizeOrder(orderGiven)
    reply(retMsg)
@app.route('/check_kitchen')
def check_kitchen():
    
    orderGiven = takeOrder()
    print(orderGiven)
    if orderGiven == "none":
        engine = pyttsx3.init()
        engine.say('please order again by reinvoking the url as i m unable to understand')
        engine.runAndWait()
        return 'please order again by reinvoking the url as i m unable to understand'

    if 'check' in orderGiven:
        print('going to check kitchen')
        img = takeImg()
        print('response from image take')
    
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(img))
        print('going to os')
    #with open("detectImage.py") as f:
     #   code = compile(f.read(), "detectImage.py", 'exec')
      #  exec(code,'','')
        try:
            exec(open("detectImage.py").read(), globals())
    # perform some task that may raise an exception
        except Exception:
            print('exception occured')
        finally:
            return img
        return 'ok'
    
def takeImg():
    url = "http://localhost:9000/take_image"
    print('method before called')
    myResponse = requests.get(url)
    print('method called')
    print(myResponse.ok)
    if(myResponse.ok):
        print('method status is ok')
        return myResponse.content
    else:
        print('error occured')
        myResponse.raise_for_status()
        return 'error occured'
    

def webc():
    driver = webdriver.Firefox(executable_path=r'C:\Amit\Software\geckodriver-v0.18.0-win64\geckodriver.exe')
    driver.get("http://www.amazon.in/Sfu-Com-Chocolate-Gift-Basket/dp/B072LDTGC7?_encoding=UTF8&portal-device-attributes=desktop&psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00")
    elm = driver.find_element_by_id('quantity')
    elm.send_keys(4)
    elm = driver.find_element_by_id('add-to-cart-button')
    elm.click()

def recognizeOrder(orderGiven):
    if orderGiven.find('check'):
        check_kitchen()
        return 'going to check kitchen and order things if not available'
    
    
if __name__ == '__main__':
    port = 8000 #the custom port you want
    app.run(host='0.0.0.0', port=port)