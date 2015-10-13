# SIM main programm
import sys, pickle, ConfigParser

# from module import *
from module import *

dataPath = "data/"
imageRoot = "/media/datenserver/media/bilder/Scans/"

# load create config
config = ConfigParser.RawConfigParser(allow_no_value = True)
config.read("create/image.ini")

db = database.Database(dataPath,"familie")
db.create(config)

s = scan.Scanner(db)
s.scan(imageRoot)