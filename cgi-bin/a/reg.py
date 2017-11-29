#!/usr/bin/python

import MySQLdb as mariadb
import cgi
import cgitb
import commands
print "Content-type:text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
name=x.getvalue('fname')
email=x.getvalue('email')
mob=x.getvalue('mob')
pas=x.getvalue('pas')
gen=x.getvalue('gen')
dob=x.getvalue('dob')
ck=x.getvalue('ck')

name = cgi.escape(name)
email = cgi.escape(email)
mob = cgi.escape(mob)
pas = cgi.escape(pas)
gen = cgi.escape(gen)
dob = cgi.escape(dob) 
ck = cgi.escape(ck)
#link for learning mariadb 
#https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04
#mariadb_connection=sqlite3.connect('localhost')
time=commands.getoutput("date")
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk") 
#cursor.execute ("DROP TABLE IF EXISTS USERS")
#cursor.execute("CREATE TABLE USERS (USERNAME VARCHAR(20) PRIMARY KEY NOT NULL,EMAIL VARCHAR(50) NOT NULL,MOBILE_NO varchar(15) NOT NULL,PASSWORD varchar(20) NOT NULL,GENDER varchar(10) NOT NULL,DOB varchar(20) NOT NULL,TIME varchar(50) NOT NULL,CK varchar(10) NOT NULL)")

print "<html><body><h4>Users Data Table</h4>"
print """<table id= "userdata" border="2">
 			<thead>
            			<th>USERNAME</th>
            			<th>EMAIL</th>
            			<th>MOBILE_NO</th>
            			<th>PASSWORD</th>
				<th>GENDER</th>
				<th>D-O-B</th>
				<th>Time</th>
				<th>Check_Box</th>
        		</thead>"""
print "<tbody>"
cursor.execute("INSERT INTO USERS(USERNAME,EMAIL,MOBILE_NO,PASSWORD,GENDER,DOB,TIME,CK) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,mob,pas,gen,dob,time,ck))
cursor.execute("SELECT * FROM USERS")
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
	#print fname
	#print "USERNAME=%s,EMAIL=%s,MOBILE_NO=%s,PASSWORD=%s,GENDER=%s,DOB=%s,CK=%s"% (USERNAME,EMAIL,MOBILE_NO,PASSWORD,GENDER,DOB,CK)
	print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(USERNAME,EMAIL,MOBILE_NO,PASSWORD,GENDER,DOB,TIME,CK)
mariadb_connection.commit()
print "</tbody></table>"
print "</body></html>"
print ""




