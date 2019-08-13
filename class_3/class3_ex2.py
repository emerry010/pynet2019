from netmiko import ConnectHandler
from getpass import getpass
from datetime import time, timedelta, datetime
from pprint import pprint 


cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}


myDevices = [cisco3, cisco4, arista1, arista2]

for i in myDevices:
    i["username"] = 'uname'
    i["password"] = 'pword'

print()
pprint(myDevices)
print()








