#!/usr/bin/python

import MySQLdb as mariadb
import os
import cgi
import cgitb

print "Content-type: text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
uid=x.getvalue('userid')
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
cursor.execute ("DROP TABLE IF EXISTS "+uid)
cursor.execute ("DROP TABLE IF EXISTS st"+uid)
try:
	cursor.execute("delete from USERS where USERNAME=%s",(uid))
	mariadb_connection.commit();
	print """
<!DOCTYPE html>
<html>
<body><center>
<p><h5>"""+uid
	print """</h5>is Sucsessfully Deleted<p>
</center>
</body>
</html>"""
	print ""
except:
	print """
<!DOCTYPE html>
<html>
<body>
<p><h5>!NO data is Deleted Try again</h5><p>
</body>
</html>"""
	print ""
	

