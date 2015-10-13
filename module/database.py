""" a standard database interface
	using plugins to access different
	database types"""

import sqlite3

class Database:
	"""main database class"""

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
			for field in structure.items(s):
				query.append(" ".join(field))


			# create query string
			query = "CREATE TABLE IF NOT EXISTS " + s + " (" + ",".join(query) + ");"
			self._c.execute(query)

		# commit changes in the database
		self._conn.commit()
		# conn.close()


	# insert data in table
	# data is a dictionary with the keys as sqlite field names
	def insert(self,table,data,option = "CREATE_NEW"):
		if self._table_exists(table):
			
			if option == "CREATE_NEW":
				query = "INSERT INTO " + table + " " + self._dict2query(data) + ";"

				self._c.execute(query)
				self._conn.commit()
				pass

			elif option == "UPDATE_IF_EXISTS":
				# query = "INSERT INTO " + table + " " + self._dict2query(data) + ";"

				# self._c.execute(query)
				# self._conn.commit()
				pass

			pass
		pass


	def select(self,query):
		pass


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
			_values.append("'" + str(value) + "'")

		return "(" + fields + ") VALUES (" + ",".join(_values) + ")"