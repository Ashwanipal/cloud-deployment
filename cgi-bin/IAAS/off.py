#!/usr/bin/python
import cgi
import os,commands
print "Content-type:text/html"

x=cgi.FieldStorage()
osn=x.getvalue("q")

A=commands.getoutput("sudo virsh destroy "+osn)
print "location:http://192.168.43.98/cgi-bin/users/profile.py"
print ""
	



