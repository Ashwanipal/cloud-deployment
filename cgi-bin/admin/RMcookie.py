#!/usr/bin/python
import MySQLdb as mariadb
import os

print "Content-type: text/html"
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]
try:
	cursor.execute("select CNO from COOKIE")
	mariadb_connection.commit()
	for CNO in cursor:
		b=CNO
		a=b[0]
		cursor.execute("delete from COOKIE where CNO=%s",(a))
		mariadb_connection.commit();
	mariadb_connection.close()
	print "location:http://192.168.43.98/cgi-bin/admin/usersDB.py"
	print ""
except:
	print "There is some problem in Server"
	print ""



