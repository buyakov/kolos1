import anvil.server
import anvil.media
import qrcode
from io import BytesIO

@anvil.server.background_task
def weather():
  # формируем запрос
  url = 'https://api.openweathermap.org/data/2.5/weather?q=Киров&units=metric&lang=ru&appid=390c8911b10d0176aeceb068d00b6940'
  # отправляем запрос на сервер и сразу получаем результат
  #weather_data = requests.get(url).json()
  weather_data = anvil.http.request(url, json=True)
  # получаем данные о температуре и о том, как она ощущается
  temperature = round(weather_data['main']['temp'])
  description = weather_data['weather'][0]['description']
  temperature_feels = round(weather_data['main']['feels_like'])
  code = weather_data['weather'][0]['icon']
  content = '{label}<img src="https://openweathermap.org/img/wn/' + code + '@2x.png" width="30" height="30"/>'
  return content
  
@anvil.server.callable
def weather_call():
  content = anvil.server.launch_background_task('weather')
  return content

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