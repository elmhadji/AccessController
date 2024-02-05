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
				CREATE TABLE IF NOT EXISTS persons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    birthday TEXT NOT NULL,
                    phone INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    encoding TEXT NOT NULL
                );
			""")
			self.connection.commit()

	def addPerson(self, name, birthday, phone, email, address, encoding):
		with self.connection:
			# Save the encoding as a string directly
			encodingStr = ",".join(map(str, encoding))
			self.connection.execute("""
				INSERT INTO persons (name, birthday, phone, email, address, encoding) VALUES (?, ?, ?, ?, ?, ?);
			""", (name, birthday, int(phone), email, address, encodingStr))
			self.connection.commit()

	def getEncodingList(self, name):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM persons WHERE name = ?;
			""", (name,))
			row = cursor.fetchone()
			if row:
				encodingStr = row[0]
				# Convert the encoding string into a list of floats
				encodingList = list(map(float, encodingStr.split(",")))
				return encodingList
			else:
				return None

	def getEncodingArray(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM persons;
			""")
			encodingList = []
			for row in cursor:
				encodingStr = row[0]
				# Remove square brackets and then split the encoding string using any whitespace as a separator
				encodingList.append(list(map(float, encodingStr.strip('[]').split())))
			return encodingList

	def getPersonNames(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT name FROM persons;
			""")
			namesList = [row[0] for row in cursor]
			return namesList
