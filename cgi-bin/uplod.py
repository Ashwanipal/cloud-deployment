#!/usr/bin/python
import commands
import cgi, os
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   	fn = os.path.basename(fileitem.filename)
	#go to the location of "/var/www/html/img/" and give permission <chmod 777 folder_name -R> and <chmod 777 img_name.png -R>
   	open('/var/www/html/images/profilpic/' + fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   	message = 'No file was uploaded'   
print """\
Content-Type: text/html\n
<html><body><p>%s</p></body></html>
""" % (message)

print "<img src='http://127.0.0.1/images/profilpic/"+fn+"'>"
print ""


