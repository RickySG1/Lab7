import os
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
from getpass import getpass

username = input("Enter your SSH Username: ")
password = getpass("Enter your SSH Password: ")

device = {
    'ip' : '192.168.108.10',
    'username' : username,
    'password' : password,
    'device_type' : 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open(f'back_configuration','x')
    f.write(output)
    f.close
except (NetMikoTimeoutException):
    print("The following has timed out: " + device['ip'])
except (AuthenticationException):
    print("Authentication failure on device: " + device['ip'])
except (SSHException):
    print("Could not connect to the device using SSH. Please check SSH settings on: " + device['ip'])

print("The Script has Completed")
