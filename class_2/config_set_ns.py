from netmiko import ConnectHandler
from getpass import getpass


device =  {
"host": "nxos2.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
#"global_delay_factor": 2,
"fast_cli": True,
}


net_connect =  ConnectHandler(**device)
print(net_connect.find_prompt())

command = 'show lldp neig detail'
output = net_connect.send_config_set(command, strip_prompt=False, strip_command=False) 
#output = net_connect.send_config_from_file(config_file='configs.txt') 

#net_connect.close()
print(output)


