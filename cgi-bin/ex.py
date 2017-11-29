#!/usr/bin/python
import os
import cgi, cgitb 
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

# Get data from fields
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('physics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"
#radio button----------------------------------------------
if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"
#txt area--------------------------------------------------
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"

#create COOKIS WIth PYTHON---------------------------------
print "Set-Cookie:UserID=XYZ;\r\n"
print "Set-Cookie:Password=XYZ123;\r\n"
print "Set-Cookie:Expires=Tuesday, 31-Dec-2020 23:12:40 GMT";\r\n"
print "Set-Cookie:Domain=www.tutorialspoint.com;\r\n"
print "Set-Cookie:Path=/perl;\n"
#Here is an example of how to retrieve cookies.------------
from os import environ
import cgi, cgitb

if environ.has_key('HTTP_COOKIE'):
   for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
      (key, value ) = split(cookie, '=');
      if key == "UserID":
         user_id = value

      if key == "Password":
         password = value

print "User ID  = %s" % user_id
print "Password = %s" % password
#----------------------------------------------------------

print "Content-type:text/html\r\n\r\n"
print ""
print "<html>"
print "<head>"
print "<title>Hello CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Text box value hear</h2>"
print "<h3>Hello %s %s</h3>" % (first_name, last_name)
print "<h2>check box value hear</h2>"
print "<h3> ChckBox Maths is : %s</h3>" % math_flag
print "<h3> CheckBox Physics is : %s</h3>" % physics_flag
print "Rdio button value hear"
print "<h2> Selected Subject is: %s</h2>" % subject
print "commants----------"
print "<h2> Entered Text Content is: %s</h2>" % text_content
print "</html>"
print "</body>"
print "</html>"

