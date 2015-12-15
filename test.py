import sys
from module import database,thesaurus
import pickle, configparser


config = configparser.RawConfigParser(allow_no_value = True)
config.read("create/thesaurus.ini")

db = database.Database("data/","familie_thes")
db.create(config)

thes = thesaurus.Thesaurus(thesdb=db,thesname="familie_thes",album="familie",verbose=True)
print (thes.get(1))
