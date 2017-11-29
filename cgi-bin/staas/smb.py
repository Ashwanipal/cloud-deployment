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


#mariadb_connection =mariadb.connect(user='root', passwd='redhat') 
#cursor = mariadb_connection.cursor()
#cursor.execute("use lk")
#commands.getoutput("sudo yum install samba samba-client")

commands.getoutput("sudo lvcreate --name "+user+"smb --size "+hd+"G myvg")
commands.getoutput("sudo mkfs.ext4 /dev/myvg/"+user+"smb")
commands.getoutput("sudo mkdir /media/"+user+"smb")
commands.getoutput("sudo mount /dev/myvg/"+user+"smb /media/"+user+"smb")
commands.getoutput("sudo useradd -s /sbin/nologin "+user+"")
commands.getoutput("sudo  echo -e '"+pas+"\n"+pas+"\n' |  smbpasswd -a "+user+"")

f1=open('/etc/samba/smb.conf','a')
f1.write("\n["+user+"]\npath = /media/"+user+"smb\nwritable = yes\nvalid users="+user+"\nbrowseable = yes")
f1.close()

commands.getoutput("systemctl restart smb")
#cursor.execute("insert into st"+user+"(STORAGETYPE,SIZE) values('SMB',%s)",(hd))
#mariadb_connection.commit()
#mariadb_connection.close()
'''
f1=open('/var/www/html/clienttar/smb.py','w+')
f1.write("\nimport commands \ncommands.getoutput('yum install cifs-utils samba-client')\ncommands.getoutput('mkdir /media/"+user+"smb')\ncommands.getoutput('mount -o username="+user+"//192.168.43.98/"+user+" /media/"+user+"smb')")
f1.close()
commands.getoutput('sudo chmod 777 /var/www/html/clienttar/smb.py')
commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_smb.tar /var/www/html/clienttar/smb.py")'''
print ""
print "<html>"
print "<p><a href='http://192.168.43.98/clienttar/"+user+"_smb.tar' download>Downlode</a> tar file for linux user and run it</p>"
print "<p>Windows users go to RUN window and type IP-->//192.168.43.98 and give username and password </p>"
print "</html>"
print ""

