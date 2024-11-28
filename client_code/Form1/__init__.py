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

    # Any code you write here will run before the form opens.
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    
    num = int(self.drop_down_1.selected_value)
    cad = [r['cadNo'] for r in app_tables.data.search(number=num)][0]
    sq = [r['square'] for r in app_tables.data.search(number=num)][0]
    
    link = anvil.http.url_decode('https://www.bcgen.com/demo/IDAutomationStreamingQRCode.aspx?ECL=L&D=ST00012|Name=НЕКОММЕРЧЕСКОЕ САДОВОДЧЕСКОЕ ТОВАРИЩЕСТВО ""КОЛОС-1""|PersonalAcc=40703810400130000655|BankName=АО КБ ""ХЛЫНОВ"", Г.КИРОВ|BIC=043304711|CorrespAcc=30101810100000000711|PayeeINN=4346026874|KPP=434501001|Purpose=ЧЛ/ЦЕЛ ВЗНОС, УЧАСТОК №' + str(num) + '|Sum=' + str(sq*100+100000) + '&MODE=B&PT=T&X=0.1&O=0&LM=0.2&V=0')
    
    self.image_1.source = link
    
    self.label_2.text = 'Участок № ' + str(num) + ',\n' + 'Кадастровый номер - ' + str(cad) + ',\nЧленский+целевой взнос - ' "{:.2f}".format((sq*100+100000)/100) + ' ₽'

    linkapi = 'https://pkk.rosreestr.ru/api/features/1/43:40:32706:' + str(num)
    
    response = anvil.http.request(linkapi, json=True)
    print(response)

    pass