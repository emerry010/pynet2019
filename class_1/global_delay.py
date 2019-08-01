from netmiko import ConnectHandler
from getpass import getpass


device =  {
"host": "nxos2.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
"global_delay_factor": 2,
}


net_connect =  ConnectHandler(**device)
print(net_connect.find_prompt())

command = 'show lldp neig detail'
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False) 

print(output)


