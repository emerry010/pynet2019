from netmiko import ConnectHandler
from getpass import getpass
from datetime import time, timedelta, datetime

device =  {
"host": "nxos2.lasthop.io", 
"username": "pyclass", 
"password": getpass(), 
"device_type": "cisco_ios",
    #"session_log": "my_session.txt",
#"global_delay_factor": 2,
}


net_connect =  ConnectHandler(**device)
print(net_connect.find_prompt())

time1 = datetime.now() 
command = 'show lldp neig detail'
output = net_connect.send_command_timing(command, delay_factor=5, strip_prompt=False, strip_command=False) 

time2 = datetime.now() 
diff = time2 - time1 

print(output)
print("Time to complete command: " + str(diff))




