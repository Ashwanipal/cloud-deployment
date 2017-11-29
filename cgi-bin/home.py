#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import os
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
print ""
print """<!DOCTYPE html>
<html>
<title>TechNext-"""+name+"""</title>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../css/w3-theme-black.css">
<link rel="stylesheet" href="../css/w3.css">
<link rel="stylesheet" href="../css/animation.css">

<body>
<div class="w3-top">
<ul class="w3-navbar w3-blue w3-xlarge">
	<li><a class="w3-indigo" href="#"><i class="fa fa-home"></i></a></li>
	<li><a class="w3-blue"><i class="fa fa-cloud"></i></a></li>
	<li class="w3-right"><a href="http://192.168.43.98/cgi-bin/logout.py" ><i class="fa fa-sign-in"></i></a></li>
</ul>
<nav class="w3-sidenav w3-light-gray w3-card-2 w3-animate-left w3-collapse" style="width:15%; display:block;">
	<div class="w3-container w3-right">
		<h4>TechNext <i class="fa fa-bars w3-xlarge"></i></h4>
	</div><br></br>
	<div class="w3-container">
		<div class="w3-container w3-center" style="width:100%;">
			<img class="w3-border w3-border-blue w3-round-xlarge" src='http://192.168.43.98/images/profilpic/"""+name+"""'  style="width:100%;" class="w3-round">
			<br><canter><h5>"""+name+"""</h5></canter>
		</div>
	</div>
	<ul class="w3-ul" method="post">
		<a href="http://192.168.43.98/cgi-bin/users/profile.py" class="w3-border-top w3-border-blue" target="my">HOME</a>
		<a href="http://192.168.43.98/saas1.html" class="w3-border-top w3-border-blue" target="my">SAAS</a>
		<a href="http://192.168.43.98/staas1.html" class="w3-border-top w3-border-blue" target="my">STAAS</a>
		<a href="http://192.168.43.98/caas1.html" class="w3-border-top w3-border-blue" target="my">CAAS</a>
		<a href="http://192.168.43.98/iaas.html" class="w3-border-top w3-border-bottom w3-border-blue" target="my">IAAS</a>
		<a href="http://192.168.43.98/eXtplorer_2.1.7/index.php" class="w3-border-bottom w3-border-blue" target="my"> MY Drive</a>	
	</ul>

</nav>
<div style="width:85%; height:20px; float:right;">
<marquee>Cloud computing is a type of Internet-based computing that provides shared computer processing resources and data to computers and other devices on demand. It is a model for enabling ubiquitous, on-demand access to a shared pool of configurable computing resources (e.g., computer networks, servers, storage, applications and services)
</marquee>
</div>
<div style="width:85.1%; height:520px; float:right;">
	<iframe src="http://192.168.43.98/cgi-bin/users/profile.py"class="w3-border w3-border-white" name="my" width="100%" height="100%"></iframe>
</div>

</div>
</div>
</body>
</html>"""
print ""
