import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

#@anvil.server.callable
#def add_row(cn, cad_cost, address, util_by_doc, cc_date_entering, area_value):
#  row = app_tables.table_2.add_row(number = int(cn[13:]), cn = cn, area_value = area_value, address = address, util_by_doc = util_by_doc, cad_cost = cad_cost, cc_date_entering = cc_date_entering)
