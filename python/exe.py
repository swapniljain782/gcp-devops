num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("+ \n - \n / \n *")
operation = input("select the operation: ")

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mul(num1, num2):
    return num1 * num2

if operation=="+":
	result = sum(num1, num2)
	print(result)
elif operation=="-":
	result = sub(num1, num2)
	print(result)
elif operation=="/":
	result = div(num1, num2)
	print(result)
elif operation=="*":
	result = mul(num1, num2)
	print(result)

#print('enter a no. to check if that is EVEN or NOT')
#
#user_input = ""
#while user_input != 'q':
#	user_input = input('Enter a no. or q for quit: ')
#	if user_input.isdigit():
#		if int(user_input) % 2 == 0:
#			print('Yes no. is Even')
#		else:
#			print('Yes no. is odd')

num = [1, 29, 40, 30, 20, 50, 29, 34]
while 29 in num:
  num.remove(29)
