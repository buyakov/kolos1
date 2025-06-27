from ._anvil_designer import Form1Template
from anvil import *
import anvil.media
# import anvil.tables as tables
# import anvil.tables.query as q
from anvil.tables import app_tables
# import anvil.server
import anvil.http

from anvil.js.window import jQuery
from anvil.js import get_dom_node

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

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_box_1.visible = False
    self.text_box_2.visible = False
    self.text_box_3.visible = False
    self.image_2.visible = False
    self.rich_text_1.visible= False
    self.linear_panel_1.visible = False
    self.linear_panel_2.visible = False
    self.grid_panel_1.visible = False
    self.status = 'Членский взнос'
    self.t1 = 0
    self.t2 = 0
    self.yandex_click = 0
    self.google_click = 0
    self.label_4.text = str(temperature) + ' °C'
    self.rich_text_2.content = content

    #self.api_url = "https://api.counterapi.dev/v1/wilted-brisk-improvement.anvil.app/my_counter/"
    
    # увеличиваем счетчик
    #response = anvil.http.request(self.api_url, json=True)
    # обновляем данные о сгенерированных кодах в разделе Общая информация
    #self.label_5.text = 'Количество сгенерированных QR кодов - ' + str(response['count'])

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""

    # api_url = "https://api.counterapi.dev/v1/wilted-brisk-improvement.anvil.app/my_counter"

    # исключаем выбор пустого значения номера участка
    if self.drop_down_1.selected_value is not None:
      # присваиваем переменной num значение из drop_down
      num = int(self.drop_down_1.selected_value)

      if self.status == 'Членский взнос':
        # получаем площадь участка из таблицы
        area_value = [r['area_value'] for r in app_tables.table_2.search(number=num)][0]
        # собираем ссылку для генерации QR кода
        link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЧЛ ВЗНОС, УЧАСТОК №' + str(num) + '|Sum=' + str(area_value*500) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
        # увеличиваем счетчик
        #response = anvil.http.request(f"{self.api_url}up", json=True)
        # передаем информацию о платеже на страницу
        self.label_2.text = 'Участок № ' + str(num) + '\nСумма к оплате - ' + str(area_value*5) + ' ₽'
        # обновляем данные о сгенерированных кодах в разделе Общая информация
        #self.label_5.text = 'Количество сгенерированных QR кодов - ' + str(response['count'])
        # передаем изображение QR кода на страницу
        self.image_1.source = link

      elif self.status == 'Электроэнергия':
        # расчитываем потребление электроэнергии
        consumption = self.t2 - self.t1
        amount = consumption * 4.5  # 4.5 руб за кВт
        if (self.text_box_1.text is not None) and (self.text_box_2.text is not None) and (consumption >= 0):
          # собираем текст для генерации QR кода
          payment_text = (
            "ST00012|"  # Версия стандарта
            "Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО \"КОЛОС-1\"|"
            "PersonalAcc=40703810400130000655|"
            "BankName=АО КБ \"ХЛЫНОВ\", Г.КИРОВ|"
            "BIC=043304711|"
            "CorrespAcc=30101810100000000711|"
            "PayeeINN=4346026874|"
            "KPP=434501001|"
            f"Purpose=ЭЛЕКТРОЭНЕРГИЯ, УЧАСТОК №{num}, Т1={self.t1}, Т2={self.t2}|"
            f"Sum={amount*100}"
          )
          qr_img = anvil.server.call('generate_qr_code', payment_text)
          # собираем ссылку для генерации QR кода
          link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЭЛЕКТРОЭНЕРГИЯ, УЧАСТОК №' + str(num) + ', Т1=' + str(self.t1) + ', Т2=' + str(self.t2) + '|Sum=' + str(consumption*4.5*100) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
          # увеличиваем счетчик
          #response = anvil.http.request(f"{self.api_url}up", json=True)
          # передаем информацию о платеже на страницу
          self.label_2.text = 'Участок № ' + str(num) + '\nПотребление, кВт - ' + str(consumption) + '\nСумма к оплате - ' + str(consumption*4.5) + ' ₽'
          # обновляем данные о сгенерированных кодах в разделе Общая информация
          #self.label_5.text = 'Количество сгенерированных QR кодов - ' + str(response['count'])
          # передаем изображение QR кода на страницу
          self.image_1.source = link
          self.image_1.source = qr_img
         
        else:
          self.label_2.text = 'Корректно введите показания'
          self.drop_down_1.selected_value = None
          self.text_box_1.text = None
          self.text_box_2.text = None
          self.image_1.source = None

      elif self.status == 'Прошлые периоды':
        if self.text_box_3.text is not None:
          # собираем ссылку для генерации QR кода
          link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ПРОШЛЫЕ ПЕРИОДЫ, УЧАСТОК №' + str(num) + '|Sum=' + str(self.payment*100) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
          # увеличиваем счетчик
          #response = anvil.http.request(f"{self.api_url}up", json=True)
          # передаем информацию о платеже на страницу
          self.label_2.text = 'Участок № ' + str(num) + '\nСумма к оплате - ' + str(self.payment) + ' ₽'
          # обновляем данные о сгенерированных кодах в разделе Общая информация
          self.label_5.text = 'Количество сгенерированных QR кодов - ' + str(response['count'])
          # передаем изображение QR кода на страницу
          self.image_1.source = link

        else:
          self.label_2.text = 'Введите сумму'
          self.drop_down_1.selected_value = None
          self.text_box_3.text = None
          self.image_1.source = None
      else:
        #собираем данные по участку из таблицы
        cn = [r['cn'] for r in app_tables.table_2.search(number=num)][0]
        area_value = [r['area_value'] for r in app_tables.table_2.search(number=num)][0]
        address = [r['address'] for r in app_tables.table_2.search(number=num)][0]
        util_by_doc = [r['util_by_doc'] for r in app_tables.table_2.search(number=num)][0]
        cad_cost = [r['cad_cost'] for r in app_tables.table_2.search(number=num)][0]
        cc_date_entering = [r['cc_date_entering'] for r in app_tables.table_2.search(number=num)][0]

        # собираем ссылку для запроса информации из Росреестра
        #linkapi = 'https://pkk.rosreestr.ru/api/features/1/43:40:32706:' + str(num)
        # делаем запрос на сайт Росреестра, работает через раз
        #response = anvil.http.request(linkapi, json=True)
        # из json файла берем нужные данные
        #cn = response['feature']['attrs']['cn'] #кадастровый номер
        #cad_cost = response['feature']['attrs']['cad_cost'] #кадастровая стоимость
        #address = response['feature']['attrs']['address'] #адрес
        #util_by_doc = response['feature']['attrs']['util_by_doc'] #тип использования
        #cc_date_entering = response['feature']['attrs']['cc_date_entering'] #дата внесения сведений о кадастровой стоимости в ГКН
        #area_value = response['feature']['attrs']['area_value'] #площадь

        #передаеем данные об участке на страницу
        self.label_2.text = 'Участок № ' + str(num) + '\n\nИнформация из Росреестра:\n' + 'Кадастровый номер - ' + str(cn) + ',\nКадастровая стоимость - ' "{:.2f}".format(cad_cost) + ' ₽\n' + 'Дата внесения сведений о кадастровой стоимости в ГКН - ' + str(cc_date_entering) + '\nАдрес - ' + str(address) + '\nТип использования - ' + str(util_by_doc) + '\nПлощадь - ' + str(area_value) + ' м²'
        #self.image_1.visible = False
        self.image_2.source = [r['plan'] for r in app_tables.table_2.search(number=num)][0]

        #запрос на сервер для добавления данных в таблицу
        #anvil.server.call('add_row', cn, cad_cost, address, util_by_doc, cc_date_entering, area_value)
    else:
      self.text_box_1.text = None
      self.text_box_2.text = None
      self.text_box_3.text = None
      self.label_2.text = None
      self.image_1.source = None
      self.image_2.source = None
      self.image_3.source = None
      self.rich_text_1.content = None
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    #сбрасываем значения полей при смене статуса
    self.text_box_1.text = None
    self.text_box_2.text = None
    self.text_box_3.text = None
    self.label_2.text = None
    self.image_1.source = None
    self.image_2.source = None
    self.image_3.source = None
    self.drop_down_1.selected_value = None
    #anvil.js.get_dom_node(self.linear_panel_1).remove()
    #сохраняем в переменную значение статуса
    self.status = self.drop_down_2.selected_value
    #устанавливаем видимость полей для статуса Членский и целевой взнос
    if self.status == 'Членский взнос':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.label_1.visible = True
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.drop_down_2.visible = True
      self.image_1.visible = True
      self.image_2.visible = False
      self.image_3.visible = False
      self.rich_text_1.visible = False
      self.grid_panel_1.visible = False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
    #устанавливаем видимость полей для статуса Электроэнергия
    if self.status == 'Электроэнергия':
      self.text_box_1.visible = True
      self.text_box_2.visible = True
      self.text_box_3.visible = False
      self.label_1.visible = True
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.drop_down_2.visible = True
      self.image_1.visible = True
      self.image_2.visible = False
      self.image_2.visible = False
      self.rich_text_1.visible= False
      self.grid_panel_1.visible = False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
    #устанавливаем видимость полей для статуса Прошлые периоды
    if self.status == 'Прошлые периоды':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = True
      self.label_1.visible = True
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.drop_down_2.visible = True
      self.image_1.visible = True
      self.image_2.visible = False
      self.image_3.visible = False
      self.rich_text_1.visible= False
      self.grid_panel_1.visible = False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
    #устанавливаем видимость полей для статуса Информация об участке
    if self.status == 'Информация об участке':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.label_1.visible = True
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.drop_down_2.visible = True
      self.image_1.visible = False
      self.image_2.visible = True
      self.image_3.visible = False
      self.rich_text_1.visible= False
      self.grid_panel_1.visible = False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
    #устанавливаем видимость полей для статуса Схема участков
    if self.status == 'Схема участков':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.label_1.visible = False
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.drop_down_2.visible = True
      self.image_1.visible = False
      self.image_2.visible = False
      self.image_3.visible = True
      self.rich_text_1.visible= False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
      self.grid_panel_1.visible = True
      # сохраняем в перменную изображение по ссылке
      link = 'https://i.postimg.cc/5bs26tpJ/Kolos-img.png'
      # добавляем изображение в контейнер на форме
      self.image_3.source = link
    #устанавливаем видимость полей для статуса Общая информация
    if self.status == 'Общая информация':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.label_1.visible = False
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.drop_down_2.visible = True
      self.image_1.visible = False
      self.image_2.visible = False
      self.image_3.visible = False
      self.rich_text_1.visible = True
      self.grid_panel_1.visible = False
      self.linear_panel_1.visible = False
      self.linear_panel_2.visible = False
      self.label_5.visible = False
    pass

  #запись переменной t1 из поля Предыдущие показания
  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    #если значение поля не пустое
    if self.text_box_1.text is not None:
      #если поле не целое или отрицательное
      if not isinstance(self.text_box_1.text, int) or self.text_box_1.text < 0:
        #то очищаем поле
        self.text_box_1.text = None
      #в противном случае присваеваем значение поля в перемнную
      else:
          self.t1 = int(self.text_box_1.text)
    pass

  #запись переменной t2 из поля Текущие показания
  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_2.text is not None:
      if not isinstance(self.text_box_2.text, int) or self.text_box_2.text < 0:
        self.text_box_2.text = None
      else:
          self.t2 = int(self.text_box_2.text)
    pass

  #запись переменной payment из поля Сумма
  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_3.text is not None:
      if not isinstance(self.text_box_3.text, int) or self.text_box_3.text < 0:
        self.text_box_3.text = None
      else:
          self.payment = int(self.text_box_3.text)
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_3.visible = False
    self.linear_panel_1.visible = True
    self.linear_panel_2.visible = False
    self.yandex_click += 1
    if self.yandex_click < 2:
      # Создаем элемент iframe
      iframe_yandex = jQuery("<iframe width='100%' height='400' frameborder='0'>").attr("src","https://yandex.ru/map-widget/v1/?um=constructor%3A8c78e07a751d5a9e657860e397d28e92a92ff8ebc0fb8a8ba7be72ea7417b931&amp;source=constructor")
      # добавляем iframe в контейнер на форме
      iframe_yandex.appendTo(get_dom_node(self.linear_panel_1))
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_3.visible = False
    self.linear_panel_1.visible = False
    self.linear_panel_2.visible = True
    self.google_click += 1
    if self.google_click < 2:
      # Создаем элемент iframe
      iframe_google = jQuery("<iframe width='100%' height='400' frameborder='0'>").attr("src","https://www.google.com/maps/d/embed?mid=1Va23cJVcImyNFZfrASGqnYF-aqVdHzQ&ehbc=2E312F&noprof=1")
      # добавляем iframe в контейнер на форме
      iframe_google.appendTo(get_dom_node(self.linear_panel_2))
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.image_3.visible = True
    self.linear_panel_1.visible = False
    self.linear_panel_2.visible = False
    pass