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
	a=cookie["TechNext"].value
	cursor.execute("select CNO from COOKIE")
	mariadb_connection.commit()
	for CNO in cursor:
		b=CNO
		if(b[0] == a):
			cursor.execute("delete from COOKIE where CNO=%s",(a))
			mariadb_connection.commit();
			break
except (Cookie.CookieError, KeyError):
	print "There is Some Problem in Server"
mariadb_connection.close()
print "location:http://192.168.43.98/"
print ""

