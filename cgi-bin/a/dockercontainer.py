#!/usr/bin/python2
import commands
ip=commands.getoutput("hostname -i")
commands.getoutput("sudo sed -i 's/172.17.0.2/"+ip+"/g' /etc/sysconfig/shellinaboxd")

#commands.getoutput("sed -s '/172.17.0.3/"+ip+"/g' etc/sysconfig/shellinaboxd")
commands.getoutput("sudo echo root | sudo passwd root --stdin ")


