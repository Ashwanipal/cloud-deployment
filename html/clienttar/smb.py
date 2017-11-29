
import commands 
commands.getoutput('yum install cifs-utils samba-client')
commands.getoutput('mkdir /media/asassmb')
commands.getoutput('mount -o username=asas//192.168.43.98/asas /media/asassmb')