from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.0.164',  #Your Server IP
    'username': 'badserver', #your Server Username
    'password': 'Solidsnake1', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
