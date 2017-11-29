#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import os
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
				
				
print ""				
print """
<html>
<title>profile</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<link rel="stylesheet" href="http://192.168.43.98/css/font-awesome.min.css">
<body>
<header class="w3-container w3-blue ">
	<center><h3>HOME</h3></center>
</header>
<div class="w3-container">
	<h4>Running instances [IAAS]</h4>
	<table class="w3-table-all">
 		<tr class="w3-light-grey">
			<th>SR_NO</th>
			<th>OSNAME</th>
            		<th>IP:PORT</th>
            		<th>CONTROLS</th>
            	</tr>
		<tbody>"""
cursor.execute("SELECT * FROM "+name)
result = cursor.fetchall()
for row2 in result:
	SR_NO = row2[0]
      	OSNAME = row2[1]
	PORT = row2[2]
	VNC_PORT = row2[3]
	print """<tr><td>%s</td> <td>%s</td> <td>192.168.43.98:%s</td> <td><a href='http://192.168.43.98/cgi-bin/IAAS/start.py?q=%s&r=%s&n=%s'><button>Start OS..</button></a><a href='http://192.168.43.98/cgi-bin/IAAS/off.py?q=%s'><button>Force off..</button></a><a href='http://192.168.43.98/cgi-bin/IAAS/remove.py?n=%s&name=%s'><button>Remove OS..</button></a></td> </tr>"""%(SR_NO,OSNAME,PORT,PORT,VNC_PORT,OSNAME,OSNAME,OSNAME,name)
mariadb_connection.commit()
print """</tbody>
</table>"""

#cursor.execute ("DROP TABLE IF EXISTS st"+name)
#cursor.execute("create table st"+name+" (STORAGETYPE varchar(37) NOT NULL, SIZE varchar(37) NOT NULL)")
print """<h4>Storage usage[STAAS]</h4>
	<table class="w3-table-all w3-half">
 		<tr class="w3-light-grey">
			<th>STORAGETYPE</th>
			<th>SIZE</th>
			<th>CONTROLS</th>
            	</tr>
		<tbody>"""
cursor.execute("SELECT * FROM st"+name)
result = cursor.fetchall()
for row2 in result:
	STORAGETYPE = row2[0]
	SIZE = row2[1]
      	if (STORAGETYPE=="NFS"):
		print """<tr><td>"""+STORAGETYPE+"""</td> <td>"""+SIZE+"""GB</td> <td><a href='http://192.168.43.98/clienttar/"""+name+"""_nfs.tar' download><button>Get access</button></a><a href='http://192.168.43.98/extend.html'><button>Extend Storage</button></a></td> </tr>"""
	if (STORAGETYPE=="DRIVE"):
		print """<tr><td>"""+STORAGETYPE+"""</td> <td>"""+SIZE+"""GB</td> <td><a href='http://192.168.43.98/eXtplorer_2.1.7/index.php'><button>Get access</button></a><a href='http://192.168.43.98/extend.html'><button>Extend Storage</button></a></td> </tr>"""
		
mariadb_connection.commit()
mariadb_connection.close()
print """</tbody>
</table>
</div>
</body>
</html>"""
print ""
