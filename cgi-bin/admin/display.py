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
#uid="avhipal"
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
try:
	cursor.execute("SELECT * FROM USERS WHERE USERNAME=%s",(uid))
	result = cursor.fetchall()
	if (result!=""):
		for row in result:
			USERNAME = row[0]
		      	EMAIL = row[1]
			MOBILE_NO = row[2]
			PASSWORD = row[3]
			GENDER = row[4]
			DOB = row[5]
			TIME = row[6]
			CK = row[7]
	mariadb_connection.commit()
	print """
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<body>
<div class="w3-container">
	<div class="w3-container w3-center  w3-margin " style="width:140px;">
		<img src='http://192.168.43.98/images/profilpic/"""+USERNAME+"""' style="width:100%;" class="w3-round"><br>
	</div>
</div>
<table border="1" >
 	<tbody>
		<tr><td>USER</td><td>"""+USERNAME+"""</td></tr>
		<tr><td>EMAIL</td><td>"""+EMAIL+"""</td></tr>
		<tr><td>MOB</td><td>"""+MOBILE_NO+"""</td></tr>
		<tr><td>PASS</td><td>"""+PASSWORD+"""</td></tr>
		<tr><td>GEN</td><td>"""+GENDER+"""</td></tr>
		<tr><td>DOB</td><td>"""+DOB+"""</td></tr>
		<tr><td>TIME</td><td>"""+TIME+"""</td></tr>
	
	</tbody>
</table>"""
	print """<h5>[IAAS] Services usage</h5>
<table border="1">
 			<thead>
				<th>NO</th>
				<th>OSNAME</th>
            			<th>PORT</th>
            			<th>VNC_PORT</th>
            		</thead>
	<tbody>"""
	cursor.execute("SELECT * FROM "+uid)
	result = cursor.fetchall()
	for row2 in result:
		SR_NO = row2[0]
	      	OSNAME = row2[1]
		PORT = row2[2]
		VNC_PORT = row2[3]
		print "<tr><td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>"%(SR_NO,OSNAME,PORT,VNC_PORT)
	mariadb_connection.commit()
	
	print """
	</tbody>
</table>"""

	print """<h4>Storage usage[STAAS]</h4>
	<table border="1">
 		<thead>
			<th>STORAGETYPE</th>
			<th>SIZE</th>
            	</thead>
		<tbody>"""
	cursor.execute("SELECT * FROM st"+uid)
	result = cursor.fetchall()
	for row2 in result:
		STORAGETYPE = row2[0]
		SIZE = row2[1]
	      	print "<tr><td>%s</td><td>%s GB</td></tr>"%(STORAGETYPE,SIZE)
	mariadb_connection.commit()
	mariadb_connection.close()
	
	print """</tbody>
	</table>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</body>
</html>"""
	print ""
except:
	print """
<!DOCTYPE html><html><body>
<center>
	<p><h3>!USER """+uid+""" is not available</h3></p><p><h4>NO data is available</h4></p>
</center>
</body></html>"""

	print ""



