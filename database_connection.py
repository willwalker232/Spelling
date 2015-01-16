
def database_swerve_db(level):
	try:
		# Creates or opens a file called mydb with a SQLite3 DB
		db = sqlite3.connect('database.db')
		# Get a cursor object
		cursor = db.cursor()
		# Check if table users does not exist and create it
		cursor.execute('''
						  CREATE TABLE IF NOT EXISTS
						  words(id INTEGER PRIMARY KEY, 
						  word TEXT, 
						  level INTEGER)
					  ''')
		# Commit the change
		db.commit()
	# Catch the exception
	except Exception as e:
		# Roll back any change if something goes wrong
		db.rollback()
		raise e
	else:
		# Close the db connection
		cursor.execute("SELECT word FROM words WHERE level=?", (level,)) #levels are 1 2 or 3
		if db.fetchall():
			cursor.execute("SELECT word FROM words WHERE level=?", (level,))
			data=db.fetchall()
			return data
		db.close()
