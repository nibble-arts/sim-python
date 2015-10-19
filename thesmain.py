import pickle, configparser

''' create and manage the thesaurus
link image keywords with the thesaurus'''

import sys
from module import database,thesaurus


# load create config
config = configparser.RawConfigParser(allow_no_value = True)
config.read("create/thesaurus.ini")

dataPath = "data/"
imagesName = "familie"
thesName = "thes_familie"
album = 1

thesdb = database.Database(dataPath,thesName)
thesdb.create(config)

imagedb = database.Database(dataPath,imagesName)
imagedb.connect()

t = thesaurus.Thesaurus (thesdb=thesdb,thesname="familie",album=album)
t.map(imagedb)

# if verbose:
# 	print ("overall images indexed: ",s.len())