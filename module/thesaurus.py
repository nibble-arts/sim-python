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

		q = '''
		select distinct t.id,t.term,t.type,t.status,t.thesname,t.scopenote,

		tb.id as bt_id,tb.term as bt,
		tn.id as nt_id,tn.term as nt,
		tr.id as rt_id,tr.term as rt,
		tuf.id as uf_id,tuf.term as uf,
		tus.id as us_id,tus.term as us

		from thesaurus as t

		left join linking as ls on ls.source=t.id
		left join thesaurus as tn on ls.destination=tn.id  and ls.type='h'

		left join linking as ld on ld.destination=t.id
		left join thesaurus as tb on ld.source=tb.id and ld.type='h'

		left join linking as lr on lr.source=t.id or lr.destination=t.id
		left join thesaurus as tr on lr.destination=tr.id  and lr.type='r'
		
		left join linking as luf on luf.destination=t.id
		left join thesaurus as tuf on luf.source=tuf.id  and luf.type='u'
		
		left join linking as lus on lus.source=t.id
		left join thesaurus as tus on lus.destination=tus.id  and lus.type='u'
		'''

		if (id):
			q += "where t.id="+id

		self._db.select(q)


		# convert retult to dict
		keys = ("id","term","type","status","thesname","scopenote","bt_id","bt","nt_id","nt","rt_id","rt","uf_id","uf","us_id","us")
		data =  {}

		r = self._db.fetch()

		# collect complete result
		while r:
			if not r:
				return False


			for k,v in zip(keys,r):

				if (v != None):
					data[k] = v

			r = self._db.fetch()


		if (self._verbose):
			print ("get term id",id)

		#data = self._db.get("thesaurus",id)
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