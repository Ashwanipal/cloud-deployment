#!/usr/bin/python

import Cookie
import MySQLdb as mariadb
import os

print "Content-type: text/html"
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")

b=[]
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	a=cookie["TechNextadmin"].value
	cursor.execute("select SRNO from ADMINCOOKIE")
	mariadb_connection.commit()
	for SRNO in cursor:
		b=SRNO
		if(b[0] == a):
			cursor.execute("delete from ADMINCOOKIE where SRNO=%s",(a))
			mariadb_connection.commit();
			break
except (Cookie.CookieError, KeyError):
	print "There is some problem in Server"
	print ""

mariadb_connection.close()
print "location:http://192.168.43.98/"
print ""

