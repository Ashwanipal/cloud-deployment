#!/usr/bin/python

import cgi
import os,commands

print "Content-type:text/html"

x=cgi.FieldStorage()
port=x.getvalue("q")
vncport=x.getvalue("r")
osn=x.getvalue("n")
A=commands.getoutput("sudo virsh start "+osn)
a=os.system("/var/www/html/websockify-master/./run "+vncport+ " 192.168.43.98:"+port+"&")

print "location:http://192.168.43.98/vnc/vnc.html?autoconnect=true&port="+vncport
print ""

#os.system("sudo virsh start "+a)
#force off
#os.system("sudo virsh destroy "+a)
#os.system("sudo virsh shutdown "+a)
