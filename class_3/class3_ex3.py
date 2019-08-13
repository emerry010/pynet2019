from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint 
import json


filename = "nxos.json" 

with open(filename) as f:
   nxos_data = json.load(f)
   print()
   pprint(nxos_data) 
   print()









