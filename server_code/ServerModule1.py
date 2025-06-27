import anvil.server
import anvil.media
import qrcode
from io import BytesIO

@anvil.server.callable
def test():
  s = 'Проверка связи от анвил'
  return s

@anvil.server.callable
def generate_qr_code(text):
  """Генерация QR-кода из текста и возврат в виде байтов."""
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
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