from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.text_box_1.visible = False

    # Any code you write here will run before the form opens.
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""

    if self.status == 'Электроэнергия':
      print('Привет')
      
    # присваиваем переменной num значение из drop_down
    num = int(self.drop_down_1.selected_value)
    
    # присваиваем переменным cad и sq значения
    # из таблицы по по переменной num
    cad = [r['cadNo'] for r in app_tables.data.search(number=num)][0] #кадастровый номер
    sq = [r['square'] for r in app_tables.data.search(number=num)][0] #площадь участка
    
    # собираем ссылку для генерации QR кода
    link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЧЛ/ЦЕЛ ВЗНОС, УЧАСТОК №' + str(num) + '|Sum=' + str(sq*100+100000) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
    # передаем изображение QR кода на страницу
    self.image_1.source = link
    
    # собираем ссылку для запроса информации из Росреестра
    linkapi = 'https://pkk.rosreestr.ru/api/features/1/43:40:32706:' + str(num)
    # делаем запрос на сайт Росреестра, работает через раз
    response = anvil.http.request(linkapi, json=True)
    
    # из json файла берем нужные данные
    cn = response['feature']['attrs']['cn'] #кадастровый номер
    cad_cost = response['feature']['attrs']['cad_cost'] #кадастровая стоимость
    address = response['feature']['attrs']['address'] #адрес
    util_by_doc = response['feature']['attrs']['util_by_doc'] #тип использования
    cc_date_entering = response['feature']['attrs']['cc_date_entering'] #дата внесения сведений о кадастровой стоимости в ГКН
    area_value = response['feature']['attrs']['area_value'] #площадь

    #передаеем данные из Росреестра на страницу
    self.label_2.text = 'Участок № ' + str(num) + ',\n' + 'Кадастровый номер - ' + str(cad) + ',\nЧленский+целевой взнос - ' "{:.2f}".format((sq*100+100000)/100) + ' ₽' + '\n\nИнформация из Росреестра:\n' + 'Кадастровый номер - ' + str(cn) + ',\nКадастровая стоимость - ' "{:.2f}".format(cad_cost) + ' ₽\n' + 'Дата внесения сведений о кадастровой стоимости в ГКН - ' + str(cc_date_entering) + '\nАдрес - ' + str(address) + '\nТип использования - ' + str(util_by_doc) + '\nПлощадь - ' + str(area_value) + ' м²'

    anvil.server.call('add_row', cn, cad_cost, address, util_by_doc, cc_date_entering, area_value)

#    row = app_tables.table_2.add_row(number = cn[13:],
#                                    cadNo = cn,
#                                    areaVol = area_value,
#                                    address = address,
#                                    util_by_doc = util_by_doc,
#                                    cad_cost = cad_cost,
#                                    cc_date_entering = cc_date_entering)
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    
    self.status = self.drop_down_2.selected_value

    if self.status == 'Членский и целевой взнос' or self.status == 'Прошлые периоды':
      self.text_box_1.visible = False
    else:
        self.text_box_1.visible = True

    #return status
    pass
