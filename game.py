
name = input("What is your name")
swag_level = 1000 
if name == "Emily":
	print("Your swag level is choddy ,0!")
else:
	print("Your swag level is chode" , swag_level)




level_number = 14
total = 4
def award(level, score):
	if score < 5:
		award = 'bronze'
	if score >= 5 and score < 8:
		award = 'silver'
	if score >= 8 and score < 11:
		award = 'gold'
	if score >= 11:
		award = 'platinum'
	
	return award
		

Badge = award(level_number,total)

print ('he \n hey')

words = ["hello", "hi", "go"]

#retrieve (10]{!
             # words from specific level
             # aaaaaaaaaaaaaaaaaaaaaaaaaaaa-aaaaaaaaaaa aaaaa%

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

