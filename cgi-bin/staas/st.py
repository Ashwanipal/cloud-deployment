#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import os
import cgi,cgitb
import base64
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
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(a))
			mariadb_connection.commit() 
			for USERNAME in cursor:
				b=USERNAME
				cursor.execute("select USERNAME from USERS where USERNAME=%s",(b[0]))
				mariadb_connection.commit()
				for USERNAME in cursor:
					b=USERNAME
					name=b[0]

except:
	mariadb_connection.close()
	print "location:http://192.168.43.98/login.html?q=sucess"
	print ""

cgitb.enable()
x=cgi.FieldStorage()
os=x.getvalue('ostp')
protocol=x.getvalue('protocol')
hd=x.getvalue('siz')
hd=str(hd)
flag=0
if(os=="1"):
	if (protocol=="1"):
		cursor.execute("select STORAGETYPE from st"+name)
		mariadb_connection.commit() 
		for STORAGETYPE in cursor:
			b=STORAGETYPE
			if (b[0] == "NFS"):
				flag=1
		if(flag==1):
			print ""
			print """<html><body><center><h1>NFS Storage alredy u have Go to home And Access it</h1></center></body></html>"""
		else:
			print "location:http://192.168.43.98/cgi-bin/staas/nfs.py?hd="+hd+"&name="+name
			print ""
	elif (protocol=="2"):
		cursor.execute("select STORAGETYPE from st"+name)
		mariadb_connection.commit() 
		for STORAGETYPE in cursor:
			b=STORAGETYPE
			if (b[0] == "DRIVE"):
				flag=1
		if(flag==1):
			print ""
			print """<html><body><center><h1>Drive Storage alredy u have Go to home And Access it</h1></center></body></html>"""
		else:
			cursor.execute("select PASSWORD from USERS where USERNAME=%s",(name))
			mariadb_connection.commit()
			for PASSWORD in cursor:
				b=PASSWORD
				pas=b[0]
			pas = base64.b64decode(pas)
			print "location:http://192.168.43.98/cgi-bin/staas/drive.py?hd="+hd+"&name="+name+"&pas="+pas
			print ""
	elif (protocol=="3"):
			cursor.execute("select PASSWORD from USERS where USERNAME=%s",(name))
			mariadb_connection.commit()
			for PASSWORD in cursor:
				b=PASSWORD
				pas=b[0]
			pas = base64.b64decode(pas)
			print "location:http://192.168.43.98/cgi-bin/staas/smb.py?hd="+hd+"&name="+name+"&pas="+pas
			print ""
else:
	print "Wrong input"


