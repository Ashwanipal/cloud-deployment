#!/usr/bin/python
import MySQLdb as mariadb
import os
import cgi
import base64
print "Content-type:text/html"
x=cgi.FieldStorage()

usr=x.getvalue('usr')
cont=x.getvalue('cont')
pas1=x.getvalue('pas1')
pas2=x.getvalue('pas2')

usr=cgi.escape(usr)
cont=cgi.escape(cont)
pas1=cgi.escape(pas1)
pas2=cgi.escape(pas2)


if((usr=="")| (pas1=="")| (pas2=="")| (cont=="")):
	print "location:http://192.168.43.98/reset.html"
	print ""
if(pas1!= pas2):
	print "location:http://192.168.43.98/reset.html"
	print ""
pas1=base64.b64encode(pas1)
connection =mariadb.connect(user='root', passwd='redhat') 
cursor =connection.cursor()
cursor.execute("use lk")
b=[]
usr=str(usr)
cont=str(cont)
	
try:
	cursor.execute("select MOBILE_NO from USERS where USERNAME=%s",(usr));
	connection.commit()
	for MOBILE_NO in cursor:
		b=MOBILE_NO
		c=b[0]
		if(c==cont):
			cursor.execute("update USERS set PASSWORD=%s where USERNAME=%s",(pas1,usr))
			connection.commit()
			connection.close()
			print "location:http://192.168.43.98/login.html"
			print ""
		else:
			connection.close()
			print "location:http://192.168.43.98/reset.html"
			print ""
except:
	connection.close()
	print "location:http://192.168.43.98/reset.html"
	print ""






		
