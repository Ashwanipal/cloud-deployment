#!/usr/bin/python2 
import os 
os.system('yum install nfs-utils -y') 
os.system('systemctl restart nfs')
os.system('setenforce 0')
os.system('iptables -F')
os.system('mkdir /media/mystorage')
os.system('mount 192.168.43.98:/media/asas  /media/mystorage')