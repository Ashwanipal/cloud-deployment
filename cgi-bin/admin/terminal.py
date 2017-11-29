#!/usr/bin/python
import commands
print "Content-type: text/html"

commands.getoutput("sudo systemctl restart shellinaboxd")
print "location:http://192.168.43.98:4200"
print ""

