# encoding=utf-8
# SIM main programm
import sys, pickle, ConfigParser

# from module import *
from module import *
import argparse


# get commandline args

'''
-h             help
-v             verbose
-r             scan recursive
-d,--depth     scan depth when -r; 0=without limit

-a,--album     album name
--album-root   set album root; mandatory for new album

--db-path      database path; default=data/
'''

parser = argparse.ArgumentParser(description='Server Side Image Management')
# parser.add_argument("--root",dest="root",type=str,help="album root path",required=True)
parser.add_argument("-v",dest="verbose",nargs="?",const=True,help="print details",default=False)
parser.add_argument("-r",dest="recurse",nargs="?",const=True,help="scan recursive")
parser.add_argument("-d","--depth",dest="depth",type=int,help="depth of recursive scan",default=1)

parser.add_argument("-a","--album",dest="album",type=str,help="album name",required=True)
parser.add_argument("--album-root",dest="albumRoot",type=str,help="set album root path")

parser.add_argument("-s","--start",dest="scanStart",type=str,help="scan start path in album root")

parser.add_argument("--db-path",dest="datapath",type=str,help="set database path; default=data/",default="data/")


args = vars(parser.parse_args())



# set args
verbose = args["verbose"]

if args["recurse"]:
	depth = args["depth"]
else:
	depth = 1

# if args["root"]:
# 	pass

albumRoot = args["albumRoot"]
albumName = args["album"]

dataPath = args["datapath"]
scanStart = args["scanStart"]




# load create config
config = ConfigParser.RawConfigParser(allow_no_value = True)
config.read("create/image.ini")

db = database.Database(dataPath,albumName)
db.create(config)

s = scan.Scanner(db,root=albumRoot,albumName=albumName)
s.scan(subdir=scanStart,depth=depth,verbose=verbose)

if verbose:
	print "overall images indexed: ",s.len()