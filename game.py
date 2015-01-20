import csv
import time 
              

def game(words):
	for each in words:
		print(each)
	time.sleep(5)
	import os
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
			
game(words)	
        

#display 10 words for 10 seconds 

#set timer for 1 minute to enter word and check if there 

