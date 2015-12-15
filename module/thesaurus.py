''' create thesaurus to link with image database '''

import sys
from module import database


class Thesaurus:

	_db = False
	_imagedb = False
	_name = ""
	_verbose = ""

	def __init__(self,thesdb,thesname,album,verbose):
		self._verbose = verbose
		self._db = thesdb
		self._thesname = thesname
		self._album = album

		self._db.connect()


	# map keywords with thesaurus
	def map (self,imagedb,verbose):
		self._imagedb = imagedb
		self._verbose = verbose

		# delete mapping table
		query = "DELETE FROM mapping"
		self._imagedb._c.execute(query)

		# get keyword list
		query = "SELECT * FROM keyword"
		self._imagedb._c.execute(query)

		keywords = self._imagedb._c.fetchall()

		for term in keywords:
			termid = self.term_exists(term[1])
			
			# term dont exist => create term from keyword and map
			if not termid:
				id = self.insert({"term":term[1],"type":"","status":"candidate","thesname":self._thesname})
				self.set_map(term=id,keyword=term[0])

			# term already exist => check mapping
			else:
				self.set_map(term=termid,keyword=termid)
				pass


	# set mapping from album to thesaurus
	def set_map(self,term,keyword):

		if (self._verbose):
			print ("map keyword ",keyword," to term ",term)

		if not (self.map_exists(term,keyword)):
			query = "INSERT INTO mapping " + self._imagedb._dict2query({"album":self._album,"keyword":keyword,"term":term}) + ";"

			self._imagedb._c.execute(query)
			self._imagedb._conn.commit()


	# get thesaurus term by id
	def get (self,id):

		if (self._verbose):
			print ("get term id",id)

		data = self._db.get("thesaurus",id)

		return data


	def map_exists(self,term,keyword):
		query = "SELECT id FROM mapping WHERE keyword='" + str(keyword) + "' and term='" + str(term) + "';"
		self._imagedb._c.execute(query)
		data = self._imagedb._c.fetchall()

		if len(data):
			return data[0][0]


	# term exists
	def term_exists (self,term):
		query = "SELECT id FROM thesaurus WHERE term='" + term + "'"
		self._db._c.execute(query)
		data = self._db._c.fetchall()

		if len(data):
			return data[0][0]


	# insert term to thesaurus
	def insert(self,data,broader="",narrower="",related=""):
		query = "INSERT INTO thesaurus " + self._db._dict2query(data) + ";"
		self._db._c.execute(query)
		self._db._conn.commit()

		return self._db._c.lastrowid


	# set broader link from term(id) to broader(id)
	def set_broader(self,term,broader):
		pass


	# set link from source to destination
	'''
	type: bt: broader
		  nt: narrower
		  rt: relation
		  us: use
		  uf: used_for
	'''
	def set_link(self,source,destination,type):
		pass