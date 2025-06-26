import anvil.server
import qrcode
from io import BytesIO

@anvil.server.callable
def generate_qr_code(text):
  """Генерация QR-кода из текста."""
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Средний уровень коррекции
    box_size=4,  # Уменьшенный размер для лучшей читаемости
    border=2,
  )
  qr.add_data(text)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")

  bio = BytesIO()
  bio.name = 'qr_code.png'
  img.save(bio, 'PNG')
  bio.seek(0)

  return bio.getvalue()