import csv
import time 
import os
              
def retrieve_words(table, level):
	cursor.execute("SELECT word FROM ? WHERE level=?", (table,level,)) #levels are 1 2 or 3
		if db.fetchall():
			cursor.execute("SELECT word FROM ? WHERE level=?", (table,level,))
			data=db.fetchall()
			return data
		db.close()

def select_rand_word(data):
	lists = []
	while (len(lists)) != 10:
		length = (len(data) - 1)
		random = random.randint(0, length)
		lists.append(data[random])
		data.remove(data[random])
		
	return lists
		
	
def game(words):
	for each in words:
		print(each)
	time.sleep(5)
	os.system('clear')
	counter = 0
	score=0
	while counter <= 10:
		check = input("Enter a word from list")
		for i in words:
			if i == check:
				print("Correct")
				score +=1
		counter+=1
	return score
        


