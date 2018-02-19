#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from cgi import escape
name = "../dane.csv"
file = open(name, "r")
print "Content-Type:text/html"
print
print """<html><head><style>
table { border: 2px solid blue; border-collapse: collapse; width: 500px; text-align: left;}
tr:nth-child(even){background-color: #e6ffff;}
#top {background-color: #ffff80;}
</style></head>"""
print "<body><table>"
print "<tr><th><div id='top'>tytul</div></th><th><div id='top'>autor</div></th><th><div id='top'>date</div></th><th><div id='top'>IP</div></th></tr>"
line = file.readline()
while line:
        data = line.split("\t")
        print "<tr><td>" + data[0]+ "</td><td>" + data[1] + "</td><td>" + data[2] + "</td><td>" + data[3] + "</td></tr>"
        line = file.readline()
print "</table>"
print "</body></html>"
file.close()
