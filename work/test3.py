import pycurl
from StringIO import StringIO
num = "asdfghjkl"

msg = "cool beans"

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://textbelt.com/text')
c.setopt(c.POSTFIELDS, 'number=%s&message=%s' %(num, msg))
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
print (body)

if "true" in body:
    print"yes"
if "false" in body:
    print"nope"
if "quota" in body:
    print"too many texts sent"
if "number" in body:
    print"Invalid phone number"    
