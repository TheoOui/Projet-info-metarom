from netmiko import ConnectHandler
import paramiko

Network_Device = { "host": "10.80.100.254",
                   "username": "cisco",
                   "password": "M0r@TeM@2020",
                   "device_type":"cisco_ios",
                  #  "secret": "M0r@TeM@2020",
}


Connect = ConnectHandler(**Network_Device)
Connect.enable ()


to_Issue = "Show vlan brief"
print(Connect.send_command(to_Issue))
print ("ajout commit")