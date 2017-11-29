#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import cgi
import random
import commands,os

print "Content-type:text/html"

try:
	a=10
	b=20
	c=a+b
	d=os.system("date")

except:
	print "location:http://192.168.43.98/"


print ""
print c
print d
