import os


num = "6103041966"

msg ='"message=cool beans"'

os.system('curl -X POST http://textbelt.com/text -d number=%s    -d %s'%(num, msg))
