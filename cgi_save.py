#!/usr/bin/python
import cgi
import os
import cgitb; cgitb.enable()
from cgi import escape
from datetime import datetime
form = cgi.FieldStorage()
text1 = form.getvalue("tytul","no data")
text2 = form.getvalue("autor","no data")
text3 = datetime.utcnow().strftime('%Y-%m-%d %H:%M')
text4 = os.environ["REMOTE_ADDR"]
name = "../dane.csv"
print "Content-Type: text/html"
print
file = open(name,"a")
text = text1+"\t"+text2+"\t" + text3 + "\t" +text4+ "\n"
file.write(text)
file.close()
