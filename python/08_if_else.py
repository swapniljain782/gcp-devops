#if 10>8:
#    print('Hey it is True')
#else:
#    print('Hey it is false')
#
#print("ENter a no. to chec if that is even or not")
#
#num = int(input('enter a no - '))
#
#if num % 2 == 0:
#    print("yes no. is even")
#else:
#    print("no. is odd")

users = ['sam', 'messi', 'ram', 'shyam']

if 'ram' in users:
    print('user exist')
else:
    print("user doesn't exist")

users = []

if users:
    print('list is not empty')
else:
    print('list is empty')

marks = int(input("num"))

if marks >= 80:
    print("1st division")
elif marks >= 60:
    print("2nd division")
else:
    print("fail")

age = 20
voter_id = True

if age >= 18:
    if voter_id:
      print('you can vote')
    else:
     print('please apply for voter id')
else:
	print('you are not eligible')

if age >=18 and voter_id:
 print('you can vote!')
else:
 print('you can not vote')
