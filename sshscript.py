###script to automate ssh login

import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import date

username = input("Enter your SSH Username")
password = getpass("Enter your SSH Password")
date = date.today().strftime("%Y_%m_%d")

device = (  
    "ip":' "192.168.108.10',
    'username' : username,
    'password' : password,
    'device_type' : 'cisco_os'
)

c = ConnectHandler(**device)

output = c.send_command("show run")

f = open(f'back_configuration{date}','x')

f.write(output)
f.close

 