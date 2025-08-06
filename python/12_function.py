print('*'*20)
print('Welcome User')
print('Thank you for signing in.....')
print('*'*20)




def userwelcome():
    print('*'*20)
    print('Welcome User')
    print('Thank you for signing in....')
    print('*'*20)

userwelcome()


def greeting(user_name, age=None, *Hobbies):
    print('*'*20)
    print(f'Welcome {user_name}')
    print(f'age is {age}')
    for hobby in Hobbies:
     print(f'Hobby is {hobby}')
    print('Thank you for singing in')
    print('*'*20)


greeting('Swapnil', 30, 'Dancing', 'shooting', 'Raju')
greeting('Mukesh', 17, 'playing', 'swiming', 'raining') 
