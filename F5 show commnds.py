from netmiko.f5.f5_linux_ssh import F5LinuxSSH
from netmiko.f5.f5_tmsh_ssh import F5TmshSSH
from _datetime import datetime
from netmiko import ConnectHandler
import time

start_time = datetime.now()
print(start_time)
F5TmshSSH = {
        'device_type': 'f5_linux',
        'ip': '192.168.13.129',
        'username': 'root',
        'password': 'nareshplay',
    }
tmshmode = input('enter the command ')
net_connect = ConnectHandler(**F5TmshSSH)
output = net_connect.send_config_set(tmshmode)
time.sleep(5)
output = net_connect.send_command('show sys ' + input('Enter clock:'))
print(output)
