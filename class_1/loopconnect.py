from netmiko import ConnectHandler
from getpass import getpass


#    "host": "cisco3.lasthop.io", 
for i in ("cisco3.lasthop.io","cisco4.lasthop.io"): 
    device =  {
        "host": i, 
        "username": "pyclass", 
        "password": getpass(), 
        "device_type": "cisco_ios",
    #"session_log": "my_session.txt",

        net_connect =  ConnectHandler(**device)
        print(net_connect.find_prompt())
}
