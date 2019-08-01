from netmiko import ConnectHandler
from getpass import getpass


device1 =  {
"host": "nxos1.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
#"global_delay_factor": 2,
"fast_cli": True,
}

device2 =  {
"host": "nxos2.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
#"global_delay_factor": 2,
"fast_cli": True,

}

#net_connect =  ConnectHandler(**device)
#print(net_connect.find_prompt())

#command = 'show lldp neig detail'
#output = net_connect.send_config_set(command, strip_prompt=False, strip_command=False) 

for i in (device1,device2):

    net_connect =  ConnectHandler(**i)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='vlan_configs.txt') 

#net_connect.close()
    print(output)
    save_out = net_connect.save_config()
    print(save_out)








