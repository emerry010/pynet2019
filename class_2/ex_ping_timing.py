from netmiko import ConnectHandler
from getpass import getpass


device =  {
"host": "cisco4.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
}


net_connect =  ConnectHandler(**device)
print(net_connect.find_prompt())

command = 'ping'
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 
output += net_connect.send_command_timing('', strip_prompt=False, strip_command=False) 

print(output)


