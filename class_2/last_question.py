from netmiko import ConnectHandler
from getpass import getpass
from datetime import time, timedelta, datetime
from pprint import pprint 
import time

password = getpass()

device =  {
"host": "cisco4.lasthop.io", 
"username": "pyclass", 
"password": password, 
"device_type": "cisco_ios",
"secret" : password,
"session_log": "my_output.txt"
}

net_connect = ConnectHandler(**device)

prompt = net_connect.find_prompt()
print(prompt)

prompt = net_connect.config_mode()
print(prompt)

prompt = net_connect.exit_config_mode()
print(prompt)

net_connect.write_channel("disable\n")
time.sleep(2)
prompt = net_connect.read_channel()
print(prompt)

prompt = net_connect.enable() 
print(prompt)



'''


print()
cmds = ["show version", "show lldp neighbors"]

for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print("#" * 80)
    print(cmd)
    print("#" * 80)
    pprint(output)
    print("#" * 80)
    print()

    if cmd == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))
'''


print()
net_connect.disconnect()




