# encoding=utf-8
# SIM main programm
import pickle, configparser

''' create and manage the thesaurus
link image keywords with the thesaurus'''

import sys
import argparse
from module import database,thesaurus

# get commandline args

'''
-h             help
-v             verbose

-a,--album     album name

-t,--thesaurus thesaurus name

--db-path      database path; default=data/
'''


parser = argparse.ArgumentParser(description='Server Side Image Management')
# parser.add_argument("--root",dest="root",type=str,help="album root path",required=True)
parser.add_argument("-v",dest="verbose",nargs="?",const=True,help="print details",default=False)
parser.add_argument("-r",dest="recurse",nargs="?",const=True,help="scan recursive")

parser.add_argument("-a","--album",dest="album",type=str,help="album name",required=True)
parser.add_argument("-t","--thesaurus",dest="thesaurus",type=str,help="thesaurus name",required=True)

parser.add_argument("--db-path",dest="datapath",type=str,help="set database path; default=data/",default="data/")


args = vars(parser.parse_args())

# set args
verbose = args["verbose"]

album = args["album"]
thesName = args["thesaurus"]

dataPath = args["datapath"]



if album == thesName:
	print ("album and thesaurus can not be named equally")
	sys.exit()


# load create configuration
config = configparser.RawConfigParser(allow_no_value = True)
config.read("create/thesaurus.ini")


# look if album exists
if not dataPath:
	dataPath = "data/"


thesdb = database.Database(dataPath,thesName)
thesdb.create(config)


imagedb = database.Database(dataPath,album)
imagedb.connect()

t = thesaurus.Thesaurus (thesdb=thesdb,thesname="familie",album=album)

try:
	t.map(imagedb=imagedb,verbose=verbose)

	if verbose:
		print ("mapping finished")

except KeyboardInterrupt:
	print ("\n\nmapping abborted")
	