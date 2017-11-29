#!/usr/bin/python2
import commands
import cgi,cgitb,random
print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
n=x.getvalue("no")
option=x.getvalue("option")
	
if (option=="1"):
	commands.getoutput("sudo systemctl restart docker")	
	i=1
	print """<!DOCTYPE html>
<html>
<title>caas</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://192.168.43.98/css/w3.css">
<link rel="stylesheet" href="http://192.168.43.98/css/font-awesome.min.css">
<body>
<header class="w3-container w3-blue"><center><h3>Containers a service</h3></center></header>
<div class="w3-container" style="width:50%; height:600px;">
<h4>All the containers have userid:root & password:root</h4>
	<table class="w3-table-all">
 		<tr class="w3-light-grey">
			<th>Containerinfo</th>
			<th>Controls</th>
            	</tr>
		<tbody>"""

	for i in range(int(n)) :
		port=0
		port=random.randint(6000,7000)
	        id1=commands.getoutput("sudo docker run -itd -p "+str(port)+":4200  caas")
		commands.getoutput("sudo docker exec -t "+id1+"  service shellinaboxd restart")
		commands.getoutput("sudo docker exec -t "+id1+"  service shellinaboxd restart")
		#commands.getoutput("sudo docker exec -t "+id1+"  service sshd restart")
		ip=commands.getoutput("sudo docker exec -t "+id1+"  hostname -i")
		
		print "<tr><td>access containers using:["+ip+"]</td>"
        	print "<td><a href='http://192.168.43.98:"+str(port)+"'target='_blank'> <button>Container " + str(i) +"</button></a></td></tr>"
		print "</p>"
	print "</tbody></table></div></body></html>"
else:
	print "<html>"
	print "Image is not availableqq"
	print "<html>"
