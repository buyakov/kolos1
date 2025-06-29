import anvil.server
#import anvil.htpp
import anvil.media
import requests
import qrcode
from io import BytesIO
import time
from datetime import datetime, timedelta

# Глобальные переменные для хранения данных
_weather_cache = {
  'temperature': None,
  'content': None,
  'last_updated': None
}

def _update_weather():
  # формируем запрос
  url = 'https://api.openweathermap.org/data/2.5/weather?q=Киров&units=metric&lang=ru&appid=390c8911b10d0176aeceb068d00b6940'
  # отправляем запрос на сервер и сразу получаем результат
  weather_data = requests.get(url).json()
  # получаем данные о температуре и о том, как она ощущается
  temperature = round(weather_data['main']['temp'])
  #description = weather_data['weather'][0]['description']
  #temperature_feels = round(weather_data['main']['feels_like'])
  code = weather_data['weather'][0]['icon']
  content = '{label}<img src="https://openweathermap.org/img/wn/' + code + '@2x.png" width="30" height="30"/>'
    
  _weather_cache.update({
    'temperature': temperature,
    'content': content,
    'last_updated': datetime.now()
  }) 
  
@anvil.server.background_task
def weather_updater():
  while True:
    _update_weather()
    time.sleep(600)

# Функция для клиента (возвращает текущие данные)
@anvil.server.callable
def get_weather():
  print(_weather_cache['last_updated'])
  # Если данные устарели (>10 минут), обновляем перед возвратом
  if (
    _weather_cache['last_updated'] is None or 
    (datetime.now() - _weather_cache['last_updated']) > timedelta(minutes=10)
  ):
    _update_weather()
    print(datetime.now() - _weather_cache['last_updated'])
    print(timedelta(minutes=10))

  return {
    'temperature': _weather_cache['temperature'],
    'content': _weather_cache['content'],
    'last_update': _weather_cache['last_updated']
  }

@anvil.server.callable
def generate_qr_code(text):
  """Генерация QR-кода из текста и возврат в виде байтов."""
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=2,
  )
  qr.add_data(text)
  qr.make(fit=True)

  img = qr.make_image()

  bio = BytesIO()
  img.save(bio, format="PNG")  # Явно указываем формат
  bio.seek(0)

  # Возвращаем BlobMedia, который Anvil умеет передавать
  return anvil.BlobMedia("image/png", bio.getvalue())