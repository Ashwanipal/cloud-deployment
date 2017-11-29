#!/usr/bin/python

import MySQLdb as mariadb
import cgi
import cgitb
import Cookie
print "Content-type:text/html"
cgitb.enable()
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk") 
#cursor.execute ("DROP TABLE IF EXISTS USERS")
#cursor.execute("CREATE TABLE USERS (USERNAME VARCHAR(20) PRIMARY KEY NOT NULL,EMAIL VARCHAR(50) NOT NULL,MOBILE_NO varchar(15) NOT NULL,PASSWORD varchar(20) NOT NULL,GENDER varchar(10) NOT NULL,DOB varchar(20) NOT NULL,TIME varchar(50) NOT NULL,CK varchar(10) NOT NULL)")
#For Users table------------------------------------------------------------------------------------------------------------
cursor.execute("SELECT * FROM USERS")
print """
<!DOCTYPE html>
<html>
<title>TechNext-userDB</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<body>
	<ul class="w3-navbar w3-blue">
		<center><h4>Users Data Table</h4></center>
	</ul>
	<table id= "userdata" border="1">
 			<thead>
				<th>USERNAME</th>
            			<th>EMAIL</th>
            			<th>MOBILE_NO</th>
            			<!--<th>PASSWORD</th>-->
				<th>GENDER</th>
				<th>D-O-B</th>
				<th>Time</th>
			</thead>
	<tbody>"""
results = cursor.fetchall()
for row in results:
	USERNAME = row[0]
      	EMAIL = row[1]
	MOBILE_NO = row[2]
	PASSWORD = row[3]
	GENDER = row[4]
	DOB = row[5]
	TIME = row[6]
	CK = row[7]
	print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(USERNAME,EMAIL,MOBILE_NO,GENDER,DOB,TIME)
mariadb_connection.commit()
print "</tbody></table>"

#cooki table----------------------------------------------------------------------------------------------------------------------------------
#cursor.execute ("DROP TABLE IF EXISTS COOKIE")
#cursor.execute("CREATE TABLE COOKIE (CNO VARCHAR(20) PRIMARY KEY NOT NULL,USERNAME VARCHAR(50) NOT NULL,PASSWORD varchar(15) NOT NULL,AUTOLOGOUT varchar(20) NOT NULL)")
print """<ul class="w3-navbar w3-blue">
		<center><h4>Users Login Logs(cookie)</h4></center>
	</ul>
<table id= "userdata1"border="1">
 			<thead>
            			<th>CNO</th>
            			<th>USERNAME</th>
            			<th>PASSWORD</th>
            			<th>AUTOLOGOUT</th>
        		</thead>
	<tbody>"""
cursor.execute("SELECT * FROM COOKIE")
result = cursor.fetchall()
for row1 in result:
	CNO = row1[0]
      	USERNAME = row1[1]
	PASSWORD = row1[2]
	AUTOLOGOUT = row1[3]
	print "<tr><td>%s</td> <td>%s</td> <td>%s</td><td>%s</td> </tr>"%(CNO,USERNAME,PASSWORD,AUTOLOGOUT)
mariadb_connection.commit()
print "</tbody></table>"
#admincooki---------------------------------------------------------------------------------------------------
#cursor.execute ("DROP TABLE IF EXISTS ADMINCOOKIE")
#cursor.execute("CREATE TABLE ADMINCOOKIE (SRNO VARCHAR(50) PRIMARY KEY NOT NULL,TIME varchar(20) NOT NULL,USERNAME varchar(15) NOT NULL,PASSWORD varchar(15) NOT NULL)")
print """<ul class="w3-navbar w3-blue">
		<center><h4>Admin Login Logs(cookie)</h4></center>
	</ul>
	<table id= "userdata1"border="1">
 			<thead>
				<th>SRNO</th>
				<th>TIME</th>
            			<th>USERNAME</th>
            			<th>PASSWORD</th>
            			
        		</thead>
	<tbody>"""
cursor.execute("SELECT * FROM ADMINCOOKIE")
result = cursor.fetchall()
for row2 in result:
	SRNO = row2[0]
      	TIME = row2[1]
	USERNAME = row2[2]
	PASSWORD = row2[3]
	print "<tr><td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>"%(SRNO,TIME,USERNAME,PASSWORD)
mariadb_connection.commit()
print "</tbody></table>"
#usertable---------------------------------------------------------------------------------------------------
uid="ashwani1pal"
#cursor.execute ("DROP TABLE IF EXISTS "+uid)
#cursor.execute("create table "+uid+" (SR_NO INTEGER PRIMARY KEY NOT NULL, OSNAME varchar(37) NOT NULL, PORT INTEGER NOT NULL, VNC_PORT INTEGER NOT NULL)");
print """<ul class="w3-navbar w3-blue">
		<center><h4>Users Data["""+uid+"""]</h4></center>
	</ul>
	<table id= "userdata1"border="1">
 			<thead>
				<th>SR_NO</th>
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
print """</tbody>
</table>
		<br><br><br><br><br><br><br><br><br><br><br><br>
		<br><br><br><br><br><br><br><br><br><br><br><br>
		<br><br><br><br><br><br><br><br><br>
</body>
</html>"""


