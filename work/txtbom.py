import pycurl
from StringIO import StringIO
import time
num = "4843889185"

msg = "GUESS WHO ;)"


for i in range(75):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://textbelt.com/text')
    c.setopt(c.POSTFIELDS, 'number=%s&message=%s' %(num, msg))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    print i
    
    if "true" in body:
        print"yes"
    if "false" in body:
        print"nope"
    if "quota" in body:
        print"too many texts sent"
    if "number" in body:
        print"Invalid phone number"    
    time.sleep(60)
