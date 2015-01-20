import time 
import random
import os
import time
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def select_rand_word(data):
	words = []
	counter=0
	while counter < 10:
		length = (len(data) - 1)
		random2 = random.randint(0, length)
		dat=str(data[random2]).lower()
		newstr=""
		for char in dat:
			if char in alphabet:
				newstr+=char
		words.append(newstr)
		data.remove(data[random2])
		counter += 1
	return words
		
def game(words):
	for each in words:
		print(each)
	time.sleep(5)
	os.system('clear')
	counter = 0
	score=0
	while counter < 10:
		check = input("Enter a word from list").lower()
		if check in words:
			print("Correct")
			words.remove(check)
			score +=1
		else:
			print("Incorrect")
		counter+=1
	return score
		
def menu():
	print("Level 1")
	print("Level 2")
	print("Level 3")
	option = input("option?")
	return option

