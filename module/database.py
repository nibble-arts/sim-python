""" a standard database interface
	using plugins to access different
	database types"""

import sqlite3,sys

class Database:
	"""main database class"""

	_tables = {}

	_dbRoot = ""
	_dbName = ""
	_conn = ""
	_c = ""

	# create sqlite db or open if exists
	# at location root
	def __init__(self,root,name):

		self._dbRoot = root
		self._dbName = name
		pass

	
	# create databse with tables
	def create(self,structure):

		# add / to root path if missing
		if not self._dbRoot.endswith("/"):
			self._dbRoot += "/"

		# create sqlite db
		self._conn = sqlite3.connect(self._dbRoot + self._dbName + ".db")
		self._c = self._conn.cursor()

		# loop all tables
		for s in structure.sections():
			query = []


			# loop all fields
			# table definition block
			table = []

			for field in structure.items(s):
				table.append(field[0])

				query.append(" ".join(field))

			self._tables[s] = table

			# query.append(table)

			# create query string
			query = "CREATE TABLE IF NOT EXISTS " + s + " (" + ",".join(query) + ");"
			self._c.execute(query)

		# commit changes in the database
		self._conn.commit()
		# conn.close()


	# insert data in table
	# data is a dictionary with the keys as sqlite field names
	def insert(self,table,data):
		if self._table_exists(table):
			
			query = "INSERT INTO " + table + " " + self._dict2query(data) + ";"

			self._c.execute(query)
			self._conn.commit()
		return self._c.lastrowid


	# update data in table by id
	# data is a dictionary with the keys as sqlite field names
	def update_by_id(self,table,id,data):
		if self._table_exists(table):
			
			query = "UPDATE " + table + " " + self._dict2update(data) + " WHERE id='" + str(id) + "';"

			self._c.execute(query)
			self._conn.commit()


	# if dataset exists, return id 
	def exists(self,table,data):

		query = "SELECT id from " + table + " " + self._dict2where(data)
		self._c.execute(query)

		data = self._c.fetchall()

		if len(data):
			return data[0][0]


	# get data from table by id
	# return a dictionary of the fields
	def get(self,table,id):
		query = "SELECT * FROM " + table + " WHERE id='" + str(id) + "'"
		self.select(query)
		data = self._c.fetchall()

		ret = {}

		for x,y in zip(data[0],self._tables[table]):
			ret[y] = x

		return ret


	# send select query
	def select(self,query):
		if query:
			self._c.execute(query)
			self._conn.commit()
	

	# return db name
	def dbName():
		return self._dbName


	# check if table exists
	def _table_exists(self,table):
		return True


	# create query from dictionary
	def _dict2query(self,data):

		fields = ",".join(data.keys())

		# add quotes to values
		_values = []

		for value in data.values():
			_values.append("'" + unicode(value) + "'")

		return "(" + fields + ") VALUES (" + ",".join(_values) + ")"


	# create where from dictionary
	def _dict2where(self,data):

		_values = []

		for key in data:
			_values.append(key + "='" + unicode(data[key]) + "'")

		return "where "+" and ".join(_values)


	# create update data string
	def _dict2update(self,data):

		_values = []

		for key in data:
			_values.append(key + "='" + unicode(data[key]) + "'")

		return "SET " + ",".join(_values)