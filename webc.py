from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?zip=560048,in&appid=a627b81715cef4aff4ad041120a71b07')
json_object = r.json()
# day1 = json_object['list'][0]['weather'][1]['main']
# day2 = json_object['list'][1]['weather'][1]['main']
# day3 = json_object['list'][2]['weather'][1]['main']
day4 = json_object['list'][3]['weather'][0]['main']
# day5 = json_object['list'][4]['weather'][1]['main']
# day6 = json_object['list'][5]['weather'][1]['main']
# day7 = json_object['list'][6]['weather'][1]['main']

driver = webdriver.Firefox(executable_path=r'C:\Amit\Software\geckodriver-v0.18.0-win64\geckodriver.exe')
# driver.get("http://www.python.org")

if day4 == 'Clouds': 
   print('Order bread chocolate')
   driver.get("http://www.amazon.in/Sfu-Com-Chocolate-Gift-Basket/dp/B072LDTGC7?_encoding=UTF8&portal-device-attributes=desktop&psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00")
   elm = driver.find_element_by_id('quantity')
   elm.send_keys(4)
   elm = driver.find_element_by_id('add-to-cart-button')
   elm.click()

if day4 == 'Clear': 
   print('Order cold drink')
elif day4 == 'Rain': 
  print('Order pizza')
  driver.get("http://www.amazon.in/Sfu-Com-Chocolate-Gift-Basket/dp/B072LDTGC7?_encoding=UTF8&portal-device-attributes=desktop&psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00")
  elm = driver.find_element_by_id('quantity')
  elm.send_keys(4)
  elm = driver.find_element_by_id('add-to-cart-button')
  elm.click()
else:
   print('do nothing')
   



