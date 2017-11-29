#!/usr/bin/python2
import commands,os
import cgi,cgitb
import MySQLdb as mariadb
print "Content-type : text/html"
cgitb.enable()
x=cgi.FieldStorage()
hd=x.getvalue('hd')
user=x.getvalue('name')
pas=x.getvalue('pas')

mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")

#1st need to create volume group(myvg)

commands.getoutput("sudo lvcreate --name D"+user+" --size "+hd+"G myvg")
commands.getoutput("sudo mkfs.ext4 /dev/myvg/D"+user+" ")
commands.getoutput("sudo mkdir /media/D"+user )
commands.getoutput("sudo chmod 777 /media/D"+user)
commands.getoutput("sudo mount /dev/myvg/D"+user+"  /media/D"+user+"")
cursor.execute("insert into st"+user+"(STORAGETYPE,SIZE) values('DRIVE',%s)",(hd))

pas1=commands.getoutput("echo -n "+pas+" | md5sum | awk '{print $1}'")

hell=("array('"+user+"','"+pas1+"','/media/D"+user+"','http://localhost','0','','3',1),")
hello=str(hell)
fo = open("/var/www/html/eXtplorer_2.1.7/config/.htusers.php", "r")
var=fo.read()
fo.close()
var=var.replace(');?>','	'+hello+'\n);?>');
fo = open("/var/www/html/eXtplorer_2.1.7/config/.htusers.php", "w")
fo.write(var)
fo.close()


#mariadb_connection.commit()
#mariadb_connection.close()
print "location:http://192.168.43.98/cgi-bin/users/profile.py"
print ""






