#                            HANGMAN BY BARNEY
#                            ================= 

# Global lists
correct_guesses = []
wrong_guesses = []
x_list = ['_']

# Input word and return it as a length of Xs
inword = input('Pick a word for the player to guess: ')
word = inword.lower()
x_word = '_ ' * len(word)
print('\n' * 50)


# Get a guess from the user and make sure its in the right form
while '_' in x_list:
	x_list = [] # This ensures the while statement doesn\'t repeat the list, but replaces it'
	usr_guess = input('Guess a letter: ')
	
	if len(usr_guess) != 1:
		print('\n')
		usr_guess = input('Your input is invalid, try again: ')
	if type(usr_guess) is not str:
		print('\n')
		usr_guess = input('Your input is invalid, try again: ')

	print('\n' * 50)

	guess = usr_guess.lower()
		
	# Show string _s with correct letter replacing the X
	if guess in word:
		if guess in correct_guesses:
			print('You already got that one!')
			print('\n' * 2)
		else:
			correct_guesses.append(guess)
	elif guess in wrong_guesses:
		print('You already guessed that, try again!')
		print('\n' * 2)
	else:
		wrong_guesses.append(guess)
	if len(wrong_guesses) == 1:
		print('  |  ')
		print('  O  ')
		print('     ')
		print('     ')
	elif len(wrong_guesses) == 2:
		print('  |  ')
		print('  O  ')
		print('  |  ')
		print('     ')
	elif len(wrong_guesses) == 3:
		print('  |  ')
		print('  O  ')
		print(' /|  ')
		print('     ')
	elif len(wrong_guesses) == 4:
		print('  |  ')
		print('  O  ')
		print(' /|\ ')
		print('     ')
	elif len(wrong_guesses) == 5:
		print('  |  ')
		print('  O  ')
		print(' /|\ ')
		print(' /   ')
	elif len(wrong_guesses) == 6:
		print('  |  ')
		print('  O  ')
		print(' /|\ ')
		print(' / \ ')
		print('\n' * 2)
		print(' You lose! Your man has been hung.')
		break
	for x in word:
	    if x in correct_guesses:
	        x_list.append(x)
	    else:
	    	x_list.append('_')

	usr_view = ' '.join(x_list)
	print('\n')
	print(usr_view)
	
	print('\n' + 'Here are your wrong guesses so far: ')
	print(' '.join(wrong_guesses))
	print('\n' + '\n')
	
	if '_' not in x_list:
		print('Congratulations you have won the game!')







