<<<<<<< HEAD
=======
import game
import database_connection
import time 
import os
import random 
import sqlite3

level=game.menu()
words=database_connection.retrieve_words(level)
words=game.select_rand_word(words)
score=game.game(words)

print (score)
>>>>>>> 808a0b04f2f9f80a72f5c5938afae6968e3da929
