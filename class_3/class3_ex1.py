from netmiko import ConnectHandler
from getpass import getpass
from datetime import time, timedelta, datetime
from pprint import pprint 


values = []


arp = net_connect.("arp_values.txt", use_textfsm=True) 

#for i in output: 
#    values.append(net_connect.("arp_values.txt", use_textfsm=True))




print(arp)


'''
for line in open('arp_data.txt'):
    sep = ' '
    line  = line.split(sep)
    values.append(line)
    print()
    pprint(line)
    print()
'''







