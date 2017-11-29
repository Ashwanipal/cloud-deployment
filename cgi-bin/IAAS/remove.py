#!/usr/bin/python
import MySQLdb as mariadb
import cgi
import os,commands

print "Content-type:text/html"

x=cgi.FieldStorage()
osn=x.getvalue("n")
name=x.getvalue("name")

mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")

h=commands.getoutput("sudo virsh destroy "+osn)
h=commands.getoutput("sudo virsh undefine "+osn)
h=commands.getoutput("sudo  rm -rf /var/lib/libvirt/images/"+osn+".qcow2")
cursor.execute("delete from "+name+ " where OSNAME=%s",(osn))
mariadb_connection.commit()
mariadb_connection.close()


print "location:http://192.168.43.98/cgi-bin/users/profile.py"
print ""

