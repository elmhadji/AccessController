import sqlite3
import numpy as np
import os

class DataBaseManager:
	def __init__(self, database_path):
		# check if the database file exists
		if not os.path.isfile(database_path):
			# if not, create a new file
			open(database_path, "w").close()
		# connect to the database file
		self.connection = sqlite3.connect(database_path)
		self.createTable()

	def createTable(self):
		with self.connection:
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS person (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL UNIQUE,
					encoding TEXT NOT NULL
				);
			""")
			self.connection.commit()

	def addPerson(self, name, encoding):
		with self.connection:
			# Save the encoding as a string directly
			encoding_str = ",".join(map(str, encoding))
			self.connection.execute("""
				INSERT INTO person (name, encoding) VALUES (?, ?);
			""", (name, encoding_str))
			self.connection.commit()

	def getEncodingList(self, name):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM person WHERE name = ?;
			""", (name,))
			row = cursor.fetchone()
			if row:
				encoding_str = row[0]
				# Convert the encoding string into a list of floats
				encoding_list = list(map(float, encoding_str.split(",")))
				return encoding_list
			else:
				return None

	def getEncodingArray(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM person;
			""")
			encoding_list = []
			for row in cursor:
				encoding_str = row[0]
				# Remove square brackets and then split the encoding string using any whitespace as a separator
				encoding_list.append(list(map(float, encoding_str.strip('[]').split())))
			return encoding_list

	def getPersonNames(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT name FROM person;
			""")
			names_list = [row[0] for row in cursor]
			return names_list
