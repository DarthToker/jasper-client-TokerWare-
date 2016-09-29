# -*- coding: utf-8-*-
import random
import re
import subprocess

import os


new_word = "BLAH"
new_message = "fuck it"

#new_name = "/home/pi/jasper/client/modules/data/%s.py" % new_word

new_name = os.path.join("client/modules", "%s.py" %new_word)


#f_old = open("/home/pi/jasper/client/modules/data/templet.txt")
f_old = open(os.path.join("client/modules/templet.txt"))

f_new = open((new_name), "w")

for line in f_old:
    f_new.write(line)
    if 'mark1' in line:
        f_new.write("new_word = '%s' \nmessage = '%s'" %(new_word, new_message))

f_old.close()
f_new.close()
