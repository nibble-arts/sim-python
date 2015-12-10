# encoding=utf-8
# SIM main programm
import sys

req_version = (3,0)
if sys.version_info >= req_version:
	import mapmain
else:
	print ("*** sim needs python version greater 3.0")