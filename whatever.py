

from random import randint

range = 1, 10
number = randint(*range)
guesses = 10

print("welcome to the game. You must guess a number between {} and {}".format(range[0], range[1]))

while guesses > 0:
	print("Haha! you have {} guesses! hit me with your best shot!".format(guesses))
  	try:
   		guess = int(raw_input(">>> "))
	except ValueError:
   		print("That's not an int!")
   		continue
  	
  	if guess == number:
  		print("YOU WIN!!!!!")
  		break

  	elif guess > number:
  		print("nice try, too high")
  		
  		
  	elif guess < number:
  		print("nice try, too low!")
  	guesses -= 1

if guesses == 0:
	print("YOU HAVE NO MORE GUESSES!!! YOU LOOOOOSE")
