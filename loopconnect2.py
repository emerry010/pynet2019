from netmiko import ConnectHandler
from getpass import getpass


#    "host": "cisco3.lasthop.io", 
device1 =  {
"host": "cisco3.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
}

device2 =  {
"host": "cisco4.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
}


for i in (device1,device2):
#    print(i)

    a = "device" + str(i)
#    print(a)

    net_connect =  ConnectHandler(**i)
    print(net_connect.find_prompt())



