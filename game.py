             
def select_rand_word(data):
	lists = []
	while (len(lists)) != 10:
		length = (len(data) - 1)
		random2 = random.randint(0, length)
		lists.append(data[random2])
		data.remove(data[random2])
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
				words.remove(i)
				score +=1
		counter+=1
	return score
        
def menu:
	print("Level 1")
	print("Level 2")
	print("Level 3")
	option = input("option?")
	return option

