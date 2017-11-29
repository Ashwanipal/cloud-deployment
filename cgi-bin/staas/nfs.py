#!/usr/bin/python2
import commands,os
import cgi,cgitb
import MySQLdb as mariadb
print "Content-type : text/html"
cgitb.enable()
x=cgi.FieldStorage()
hd=x.getvalue('hd')
user=x.getvalue('name')

mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
cursor = mariadb_connection.cursor()
cursor.execute("use lk")

#1st need to create volume group(myvg)

commands.getoutput("sudo lvcreate --name "+user+" --size "+hd+"G myvg")
commands.getoutput("sudo mkfs.ext4 /dev/myvg/"+user+" ")
commands.getoutput("sudo mkdir /media/"+user )
commands.getoutput("sudo chmod 777 /media/"+user)
commands.getoutput("sudo mount /dev/myvg/"+user+"  /media/"+user+"")
hell=commands.getoutput("sudo echo /media/"+user+ " *\(rw,no_root_squash,sync\) >> /etc/exports")
commands.getoutput("sudo exportfs -r")
commands.getoutput("systemctl restart rpcbind")
commands.getoutput("systemctl disable firewalld")
commands.getoutput("iptables -F")
commands.getoutput("systemctl restart nfs")

cursor.execute("insert into st"+user+"(STORAGETYPE,SIZE) values('NFS',%s)",(hd))
mariadb_connection.commit()
mariadb_connection.close()
	
f1=open('/var/www/html/clienttar/staasclient.py','w+')
f1.write("#!/usr/bin/python2 \nimport os \nos.system('yum install nfs-utils -y') \nos.system('systemctl restart nfs')\nos.system('setenforce 0')\nos.system('iptables -F')\nos.system('mkdir /media/mystorage')\nos.system('mount 192.168.43.98:/media/"+user+"  /media/mystorage')")  
f1.close()
commands.getoutput('sudo chmod 777 /var/www/html/clienttar/staasoclient.py')
commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_nfs.tar  /var/www/html/clienttar/staasclient.py")
print "location:http://192.168.43.98/cgi-bin/users/profile.py"
print ""





