from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.text_box_1.visible = False
    self.text_box_2.visible = False
    self.text_box_3.visible = False
    self.rich_text_1.visible= False
    self.status = 'Членский и целевой взнос'
    self.t1 = 0
    self.t2 = 0

    # Any code you write here will run before the form opens.
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""

    # исключаем выбор пустого значения номера участка
    if self.drop_down_1.selected_value is not None:
      # присваиваем переменной num значение из drop_down
      num = int(self.drop_down_1.selected_value)

      if self.status == 'Членский и целевой взнос':
        self.image_1.visible = True
        # получаем площадь участка из таблицы
        area_value = [r['area_value'] for r in app_tables.table_2.search(number=num)][0]
        # собираем ссылку для генерации QR кода
        link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЧЛ/ЦЕЛ ВЗНОС, УЧАСТОК №' + str(num) + '|Sum=' + str(area_value*100+100000) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
        # передаем информацию о платеже на страницу
        self.label_2.text = 'Участок № ' + str(num) + '\nЧленский взнос - ' + str(area_value) + ' ₽' + '\nЦелевой взнос - ' + str(1000) + ' ₽' + '\nСумма к оплате - ' + str(area_value+1000) + ' ₽'
        # передаем изображение QR кода на страницу
        self.image_1.source = link
        self.image_2.visible = False

      elif self.status == 'Электроэнергия':
        self.image_1.visible = True
        # расчитываем потребление электроэнергии
        consumption = self.t2 - self.t1
        if (self.text_box_1.text is not None) and (self.text_box_2.text is not None) and (consumption >= 0):
          # собираем ссылку для генерации QR кода
          link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЭЛЕКТРОЭНЕРГИЯ, УЧАСТОК №' + str(num) + ', Т1=' + str(self.t1) + ', Т2=' + str(self.t2) + '|Sum=' + str(consumption*4.5*100) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
          # передаем информацию о платеже на страницу
          self.label_2.text = 'Участок № ' + str(num) + '\nПотребление, кВт - ' + str(consumption) + '\nСумма к оплате - ' + str(consumption*4.5) + ' ₽'
          # передаем изображение QR кода на страницу
          self.image_1.source = link
          self.image_2.visible = False
        else:
          self.label_2.text = 'Корректно введите показания'
          self.drop_down_1.selected_value = None
          self.text_box_1.text = None
          self.text_box_2.text = None
      elif self.status == 'Прошлые периоды':
        self.image_1.visible = True
        if self.text_box_3.text is not None:
          # собираем ссылку для генерации QR кода
          link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ПРОШЛЫЕ ПЕРИОДЫ, УЧАСТОК №' + str(num) + '|Sum=' + str(self.payment*100) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
          # передаем информацию о платеже на страницу
          self.label_2.text = 'Участок № ' + str(num) + '\nСумма к оплате - ' + str(self.payment) + ' ₽'
          # передаем изображение QR кода на страницу
          self.image_1.source = link
          self.image_2.visible = False
        else:
          self.label_2.text = 'Введите сумму'
          self.drop_down_1.selected_value = None
          self.text_box_3.text = None
      else:
        #собираем данные по участку из таблицы
        self.image_2.visible = True
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
        self.image_1.visible = False
        self.image_2.source = [r['plan'] for r in app_tables.table_2.search(number=num)][0]
        
        #запрос на сервер для добавления данных в таблицу
        #anvil.server.call('add_row', cn, cad_cost, address, util_by_doc, cc_date_entering, area_value)

    else:
      self.image_1.source = None
      self.label_2.text = None
      self.text_box_1.text = None
      self.text_box_2.text = None
      self.text_box_3.text = None
      self.image_1.source = None
      self.image_2.source = None

    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    #сбрасываем значения полей при смене статуса
    self.label_2.text = None
    self.text_box_1.text = None
    self.text_box_2.text = None
    self.text_box_3.text = None
    self.image_1.source = None
    self.image_2.source = None
    #сохраняем в переменную значение статуса
    self.status = self.drop_down_2.selected_value
    #сбрасываем поле выбора номера участка при смене статуса
    self.drop_down_1.selected_value = None
    #устанавливаем видимость полей для статуса Членский и целевой взнос
    if self.status == 'Членский и целевой взнос':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.drop_down_1.visible = True
      self.label_1.visible = True
      self.label_2.visible = True
      self.rich_text_1.visible= False
    #устанавливаем видимость полей для статуса Электроэнергия
    if self.status == 'Электроэнергия':
      self.text_box_1.visible = True
      self.text_box_2.visible = True
      self.text_box_3.visible = False
      self.drop_down_1.visible = True
      self.label_1.visible = True
      self.label_2.visible = True
      self.rich_text_1.visible= False
    #устанавливаем видимость полей для статуса Прошлые периоды
    if self.status == 'Прошлые периоды':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = True
      self.drop_down_1.visible = True
      self.label_1.visible = True
      self.label_2.visible = True
      self.rich_text_1.visible= False
    #устанавливаем видимость полей для статуса Информация об участке
    if self.status == 'Информация об участке':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.drop_down_1.visible = True
      self.label_1.visible = True
      self.label_2.visible = True
      self.rich_text_1.visible= False
    #устанавливаем видимость полей для статуса Схема участков
    if self.status == 'Схема участков':
      self.image_1.visible = True
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.drop_down_1.visible = False
      self.label_1.visible = False
      self.rich_text_1.visible= False
      link = 'https://i.postimg.cc/5bs26tpJ/Kolos-img.png'
      self.image_1.source = link
      self.image_2.visible = False
      
    if self.status == 'Контакты и реквизиты':
      self.text_box_1.visible = False
      self.text_box_2.visible = False
      self.text_box_3.visible = False
      self.label_1.visible = False
      self.label_2.visible = False
      self.drop_down_1.visible = False
      self.label_1.visible = False
      self.image_1.visible = False
      self.image_2.visible = False
      self.rich_text_1.visible = True
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_1.text is not None:
      if not isinstance(self.text_box_1.text, int) or self.text_box_1.text < 0:
        self.text_box_1.text = None
      else:
          self.t1 = int(self.text_box_1.text)

    pass

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_2.text is not None:
      if not isinstance(self.text_box_2.text, int) or self.text_box_2.text < 0:
        self.text_box_2.text = None
      else:
          self.t2 = int(self.text_box_2.text)
    pass

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_3.text is not None:
      if not isinstance(self.text_box_3.text, int) or self.text_box_3.text < 0:
        self.text_box_3.text = None
      else:
          self.payment = int(self.text_box_3.text)
    pass

    def __init__(self, **properties):
      self.init_components(**properties)
    
      # Call the JavaScript function and pass the ID of the component
      anvil.js.call_js('setNumericKeyboard', self.text_box_1)
      anvil.js.call_js('setNumericKeyboard', self.text_box_2)
      anvil.js.call_js('setNumericKeyboard', self.text_box_3)
