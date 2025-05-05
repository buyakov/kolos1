#import anvil.tables as tables
#import anvil.tables.query as q
#from anvil.tables import app_tables
#import anvil.server
#import segno
#import requests
#from bs import BeautifulSoup

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

#@anvil.server.callable
#def qr_gen(data):
#  qrcode = segno.make(data,mode="byte",error='L')
#  img = qrcode.to_pil(scale=4,border=0)
#  return img

#@anvil.server.callable
#def weather():
#  url_yandex = 'https://yandex.com.am/pogoda?lat=58.55879211&lon=49.50606537'
#  response = requests.get(url_yandex).json()
#  bs = BeautifulSoup(response.text,"lxml")
#  print(bs)
