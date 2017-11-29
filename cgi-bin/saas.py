#!/usr/bin/python2
import Cookie
import MySQLdb as mariadb
import commands
import cgi,cgitb
import os
print "Content-type : text/html"
cgitb.enable()
x=cgi.FieldStorage()
sw=x.getvalue("saas")

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

commands.getoutput("systemctl restart sshd")
f1=open('../html/clienttar/saasclient.py','w')
f1.write("#!/usr/bin/python2 \nimport os \nos.system('yum install openssh-clients') \nos.system('systemctl restart sshd')\nos.system('ssh  -X root@192.168.43.98 "+sw+"') ")  
f1.close()
commands.getoutput("sudo chmod 777 /var/www/html/saasclient.txt")      
commands.getoutput("sudo tar -cvf ../html/clienttar/"+name+sw+"_saas.tar ../html/clienttar/saasclient.py")
sw=str(sw)
print ""
print """
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<link rel="stylesheet" href="http://192.168.43.98/css/font-awesome.min.css">
	<body>
	<header class="w3-container w3-blue"><center><h3>Software a service</h3></center></header>
		</br>
		<div class="w3-container">
			<center>
			<h4>Steps for access Software</h4>
			<p> Downlode the file, linux users Run the file</p>
			<img src='http://192.168.43.98/images/"""+sw+"""' class="w3-round-small"></br>
			<p><a href='http://192.168.43.98/clienttar/"""+name+sw+"""_saas.tar' download><button>"""+sw+""" is Ready to Access</button></a></p>
			<center>
		</div>
	</body>
</html>"""





	




 		











