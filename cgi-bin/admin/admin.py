#!/usr/bin/python
import Cookie
import MySQLdb as mariadb
import os
print "Content-type: text/html"
print ""
mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")
b=[]

try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	a=cookie["TechNextadmin"].value
	cursor.execute("select SRNO from ADMINCOOKIE")
	mariadb_connection.commit()
	for SRNO in cursor:
		b=SRNO
		if(b[0] == a):
			cursor.execute("select TIME from ADMINCOOKIE where SRNO=%s",(a))
			mariadb_connection.commit() 
			for TIME in cursor:
				b=TIME
				time=b[0]
except(Cookie.CookieError, KeyError):
	mariadb_connection.close()
	print "location:http://192.168.43.98/login.html?q=sucess"
	print ""

print """<!DOCTYPE html>
<html>
<title>TechNext-admin</title>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="http://192.168.43.98/css/w3-theme-black.css">
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<link rel="stylesheet" href="http://192.168.43.98/css/animation.css">
<body>
<div class="w3-top">

<ul class="w3-navbar w3-blue w3-xlarge w3-border">
	<li><a class="w3-green" href="#"><i class="fa fa-home"></i></a></li>
	<li><a class="w3-blue"><i class="fa fa-cloud"></i></a></li>
	<li class="w3-right"><a href="http://192.168.43.98/cgi-bin/admin/adminlogout.py" ><i class="fa fa-sign-in"></i></a></li>
</ul>
<nav class="w3-sidenav w3-light-grey w3-card-2 w3-animate-left w3-collapse" style="width:15%; display:block;">
	<div class="w3-container">
		"""+a+"""
		<h5 class="w3-border-bottom w3-border-gray"><center>"""+time+"""</center></h5>
	</div>
	<h5 class="w3-container w3-light-blue">ADMIN-Controls</h5>
	<ul class="w3-ul">
		<a href="http://192.168.43.98/cgi-bin/admin/usersDB.py" class="tablink w3-border-top w3-border-gray" target="my1">User's Database</a>
		<a href="http://192.168.43.98/cgi-bin/admin/hd.py" class="tablink w3-border-top w3-border-gray" target="my1">Server hardware info</a>
		<a href="http://192.168.43.98/cgi-bin/admin/terminal.py" class="tablink w3-border-top w3-border-gray" target="my1">Root Terminal</a>
		<a href="http://192.168.43.98/eXtplorer_2.1.7/index.php" class="tablink w3-border-bottom w3-border-top w3-border-gray" target="my1">Drive</a>	
	</ul>
	<h5 class="w3-container w3-light-blue">ADMIN-Controls</h5>
	<form name="rm" target="my1">
		<button onclick="return RMuser()">Remove All Cookie</button>
	</form>

</nav>
	<script>
	function RMuser() {
		var r = confirm("Press OK To Remove");
			if (r){
        			document.rm.action="http://192.168.43.98/cgi-bin/admin/RMcookie.py";
			}else{return false;}
   	document.rm.submit()
   	}
	function submitFunction(i) {
	var x = document.forms["theForm"]["userid"].value;
	if (i==1) {
		if (x == "") {
			alert("Enter the user name")
			target=blank;}
		else{
			document.theForm.action="http://192.168.43.98/cgi-bin/admin/display.py";}
	}
	if (i==2) {
    		if (x == "") {
			alert("Enter the user name")
			target=blank;}
    		else{
			var r = confirm("Press OK To Remove : "+x);
    			if (r == true) {
        			document.theForm.action="http://192.168.43.98/cgi-bin/admin/removeuser.py";}
    			else {
        			target=blank;
    			}
		}
	}
   	document.theForm.submit()
   	}
	</script>

<div style="width:85.1%; height:700px; float:right;">
	<iframe src="http://192.168.43.98/cgi-bin/admin/usersDB.py" class="w3-border w3-border-white" name="my1" width="75%" height="100%"></iframe>
	<div class="w3-rest" style="width:25%; height:100%; float:right;">
		<form name="theForm" target="my2">
			<div class="w3-rest">
			<input class="w3-input w3-border" name="userid" type="text" placeholder="Enter User Name for Search Record" required>
			<input type="button" value="Show" onClick="submitFunction(1)">
			<input type="button" value="Remove" onClick="submitFunction(2)">
			</div>
		</form>
		<iframe class="w3-border" name="my2" width="100%" height="90%"></iframe>
	</div>
</div>

</br></br></br></br></br></br></br></br></br></br></div>
</body>
</html>
"""
print ""
