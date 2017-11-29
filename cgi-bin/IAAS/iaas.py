#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import cgi,cgitb
import random
import commands
import os

print "Content-type:text/html"
cgitb.enable()
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
				uid=b[0]

except(Cookie.CookieError, KeyError):
	mariadb_connection.close()
	print "location:http://192.168.43.98/login.html?q=sucess"
	print ""

#GetALLOSINFO---------------------------------------------------------------------------------------------
x=cgi.FieldStorage()
osname=x.getvalue('OSNAME')
os=x.getvalue('OS_TYPE')
ram=x.getvalue('RAM')
cpu=x.getvalue('CPU')

#(SR_NO,OSNAME,PORT,VNC_PORT)--------------------------
cursor.execute("select SR_NO from "+uid)
mariadb_connection.commit()
count=1
for SR_NO in cursor:
	count+=1

#portno-------------------------------------------------
def func1():
	z=random.randint(5900,9999)
	cursor.execute("select PORT from "+uid)
	mariadb_connection.commit()
	for PORT in cursor:
		b=PORT
		if(z==b[0]):
			func1()
	return z
#VNCPORT------------------------------------------------			
def func2():
	y=random.randint(1000,9999)
	cursor.execute("select VNC_PORT from "+uid)
	mariadb_connection.commit()
	for VNC_PORT in cursor:
		b=VNC_PORT
		if(y==b[0]):
			func2()
	return y
port=func1()
vncport=func2()

if(os=="1"):
	osn="win7"+osname
	iso="win7.qcow2"
	img="win7.jpg"
elif(os=="2"):
	osn="win8"+osname
	iso=""
elif(os=="3"):
	osn="win10"+osname
	iso=""
elif(os=="4"):
	osn="rhel7"+osname
	iso="rhel7.1.qcow2"
	img="rhel7.png"
port=str(port)
vncport=str(vncport)
#checkifosnameisaredyexist--------------------------------------
flag=1
cursor.execute("select OSNAME from "+uid)
mariadb_connection.commit()
for osnam in cursor:
	b=osnam
	if(b[0] == osn):
		flag=0
if(flag==1):
	cursor.execute("insert into "+uid+ "(SR_NO,OSNAME,PORT,VNC_PORT) values(%s,%s,%s,%s)",(count,osn,port,vncport))
	mariadb_connection.commit()
	mariadb_connection.close()
	h=commands.getoutput("sudo qemu-img create -f qcow2 -b  /var/lib/libvirt/images/"+iso+"   /var/lib/libvirt/images/"+osn+".qcow2")
	h1=commands.getoutput("sudo virt-install --name "+osn+" --ram "+ram+" --vcpu 1 --disk=/var/lib/libvirt/images/"+osn+".qcow2 --import --noautoconsole --graphics=vnc,listen=0.0.0.0,port="+port)
	print """
<!DOCTYPE html>
<html>
<body>
<div class="w3-container">
	<center><img src='http://192.168.43.98/images/"""+img+"""' class="w3-round-small" style="width:30%">
	<center>
	<h4>Your OS is Ready to use <h4><a href='http://192.168.43.98/cgi-bin/users/profile.py '><button>Go HOME to OS controls</button></a>
</div>
</body>
</html>
"""
else:
	print ""
	print "</br></br><h4>!!"+osn+" os instance is alredy inuse</h4>"











