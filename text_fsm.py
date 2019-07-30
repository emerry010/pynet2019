from netmiko import ConnectHandler
from getpass import getpass
from datetime import time, timedelta, datetime

device =  {
"host": "cisco4.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
#"global_delay_factor": 2,
}


net_connect =  ConnectHandler(**device)
print(net_connect.find_prompt())

time1 = datetime.now() 
command = 'show version'
command2 = 'show lldp neig'

output1 = net_connect.send_command_timing(command, use_textfsm=True, strip_prompt=False, strip_command=False) 
output2 = net_connect.send_command_timing(command2, use_textfsm=True, strip_prompt=False, strip_command=False) 

re_values = output2

time2 = datetime.now() 
diff = time2 - time1 

#print(output1)

#print(str(output2['neighbor_interface']))
#print(str(output2['neighbor_interface']))
#print(output2)

#print(output2['neighbor_interface'])
#print(output2.values())

print(re_values.values())

print("\nTime to complete command: " + str(diff))




