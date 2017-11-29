#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import commands,os
import cgi,cgitb
print "Content-type: text/html"

mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]

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
'''
except:
	mariadb_connection.close()
	print "location:http://192.168.43.98/login.html?q=sucess"
	print ""
'''
cgitb.enable()
x=cgi.FieldStorage()
hd=x.getvalue('exsiz')
commands.getoutput("sudo lvextend --size +"+hd+"G /dev/myvg/"+name)
commands.getoutput("sudo resize2fs /dev/myvg/"+name)
cursor.execute("select SIZE from st"+name+" where STORAGETYPE='NFS'")
for SIZE in cursor:
	b=SIZE
	hd1=b[0]
hd=int(hd)
hd1=int(hd1)
hd=hd+hd1
hd=str(hd)
cursor.execute("update st"+name+" set SIZE="+hd+" where STORAGETYPE='NFS'")
mariadb_connection.commit()
mariadb_connection.close()
print  "location:http://192.168.43.98/cgi-bin/users/profile.py"
print  ""



