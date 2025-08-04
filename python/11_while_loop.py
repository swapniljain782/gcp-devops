print('enter a no. to check if that is EVEN or NOT')

user_input = ""
while user_input != 'q':
	user_input = input('Enter a no. or q for quit: ')
	if user_input.isdigit():
		if int(user_input) % 2 == 0:
			print('Yes no. is Even')
		else:
			print('Yes no. is odd')
