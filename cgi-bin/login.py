#!/usr/bin/python2
import MySQLdb as mariadb
import Cookie
import random
import cgi
import cgitb
import datetime
import os
import base64
print "Content-type: text/html"
cgitb.enable()
x=cgi.FieldStorage()
uid=x.getvalue('usr')
pas=x.getvalue('passwd')

uid = cgi.escape(uid)
pas = cgi.escape(pas)

mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
#---------------------------------------------------------------------------------------------------------
if (uid=="admin") and (pas=="admin"):
	z=random.randint(0,1000000000)
	tim=datetime.datetime.now()+datetime.timedelta(minutes=1)
	cookie=Cookie.SimpleCookie()
	cookie["TechNextadmin"]=z
	cookie['TechNextadmin']['expires'] = tim.strftime("%a, %d %b %Y %H:%M:%S GMT")
	print cookie
	cursor.execute("insert into ADMINCOOKIE (SRNO,TIME,USERNAME,PASSWORD) values(%s,%s,%s,%s)",(z,tim,uid,pas))
	print "location:http://192.168.43.98/cgi-bin/admin/admin.py?q=sucess"
	print ""
#--------------------------------------------------------------------------------------------------------
pas = base64.b64encode(pas)
cursor.execute("select USERNAME from USERS")
mariadb_connection.commit()
a=[]
b=[]
flag=0
for USERNAME in cursor :
	a=USERNAME ;
	if(uid==a[0]):
		cursor.execute("select PASSWORD from USERS where USERNAME=%s",(uid))
		mariadb_connection.commit()
		for PASSWORD in cursor :
			b=PASSWORD ;
		if(b[0]==pas):
			flag=1;
			break
if(flag==0):
	print "location:http://192.168.43.98/login.html?q=sucess"
	print ""
else:
	z=random.randint(0,1000000000)
	future=datetime.datetime.now()+datetime.timedelta(days=1)
	cursor.execute("insert into COOKIE(CNO,USERNAME,PASSWORD,AUTOLOGOUT) values(%s,%s,%s,%s)",(z,uid,pas,future))
	mariadb_connection.commit()
	cookie=Cookie.SimpleCookie()
	cookie["TechNext"]=z
	print cookie
	print "location:http://192.168.43.98/cgi-bin/home.py"
	print ""


