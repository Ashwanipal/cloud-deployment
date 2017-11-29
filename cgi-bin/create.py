#!/usr/bin/python2
import MySQLdb as mariadb
import commands
import os,cgitb
import cgi
import commands
import base64

cgitb.enable()
x = cgi.FieldStorage()
fileitem = x['filename']
fn=x.getvalue('usr')
ln=x.getvalue('usr1')
email=x.getvalue('email')
ph=x.getvalue('mob')
p1=x.getvalue('passwd')
p2=x.getvalue('passwd1')
dd=x.getvalue('dd')
mm=x.getvalue('mm')
yy=x.getvalue('yy')
gen=x.getvalue('gender')
ck=x.getvalue('security')
#--------------------------------------------
fn=str(fn)
ln=str(ln)
uid=fn+ln
a="-"
dd=str(dd)
mm=str(mm)
yy=str(yy)
dob=dd+a+mm+a+yy
#--------------------------------------------
uid = cgi.escape(uid)
email = cgi.escape(email)
ph = cgi.escape(ph)
p1 = cgi.escape(p1)
p2 = cgi.escape(p2)
gen = cgi.escape(gen)
dob = cgi.escape(dob)
if fileitem.filename:
   	fn = os.path.basename(uid)
	#<chmod 777 folder_name -R> and <chmod 777 img_name.png -R>
   	open('/var/www/html/images/profilpic/' + fn, 'wb').write(fileitem.file.read())
	m = 'The file "' + fn + '" was uploaded successfully'
   
else:
   	m = 'No file was uploaded' 

if((p1 != p2) | (uid == "") | (email == "") | (ph == "") | (p1 == "")| (p2 == "") | (gen == "")| (dob == "")| (ck != "on")):
	print "location:http://127.0.0.1/login.html?q=sucess"
	print ""

p1=base64.b64encode(p1)
  
time=commands.getoutput("date")
a=[]
flag=0
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk") 
cursor.execute("select USERNAME from USERS")
mariadb_connection.commit()
for USERNAME in cursor :
	a=USERNAME ;
	if(a[0] == uid):
		flag=1
		break;
if(flag==1):
	mariadb_connection.close()		
	message="This user is already Exist"
else:
	cursor.execute("INSERT INTO USERS(USERNAME,EMAIL,MOBILE_NO,PASSWORD,GENDER,DOB,TIME,CK) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(uid,email,ph,p1,gen,dob,time,ck))
	cursor.execute("create table "+uid+ " (SR_NO INTEGER PRIMARY KEY NOT NULL, OSNAME varchar(37) NOT NULL, PORT INTEGER NOT NULL, VNC_PORT INTEGER NOT NULL)");
	cursor.execute("create table st"+uid+" (STORAGETYPE varchar(37) NOT NULL, SIZE varchar(37) NOT NULL)")
	mariadb_connection.commit()
	mariadb_connection.close()
	#os.system("sudo useradd "+uid)
	#commands.getoutput("sudo echo "+p1+ "| sudo passwd "+uid+ " --stdin")	
	message="Registration sucsessfull Go to home page and DO Login"

print "Content-type: text/html"
print """
<html><body><h1>user = %s is created </h1><h1>%s<br>%s</h1></body></html>
""" %(uid,message,m)
print ""

