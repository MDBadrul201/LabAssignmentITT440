import os
from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.104',  #VM server IP
    'username': 'badserver', #server username
    'password': 'Solidsnake1', #server password 
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)

output = net_connect.send_command('apt-get update')
os.system(output)
print(output)
