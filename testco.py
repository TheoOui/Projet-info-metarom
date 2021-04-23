import netmiko
import paramiko

connection= netmiko.ConnectHandler( ip="10.80.100.254", device_type="tezst", username="cisco", password="M0r@TeM@2020")