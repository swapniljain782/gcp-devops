user_list = ['swap', 'esha', 'shrey', 'shrut']
print(user_list)

print(user_list[0])  # Accessing the first element
print(user_list[1])  # Accessing the second element

print(user_list)  # List after deletion

user_list.insert(2, 'siddharth')  # Inserting a new user at index 2
user_list.append('new_user')  # Adding a new user
print(user_list)  # List after appending a new user

del user_list[5]  # Deleting the second user
print(user_list)  # List after deletion

user_list.sort()  # Sorting the list
print(user_list)  # List after sorting

print(len(user_list))  # Length of the list 

user_list.reverse()
print(user_list)

user_list.sort(reverse=True)  # Sorting the list in reverse order
print(user_list)  # List after reverse sorting

user_list.pop()  # Removing the last element
user_list.pop(2)  # Removing the element at index 2
print(user_list)  # List after popping the last element
user_list.append('esha')
print(user_list.remove('swap'))  # Removing 'swap' from the list
print(user_list)  # List after removing 'swap'
print(user_list.count('esha'))  # Counting occurrences of 'esha'
print(user_list.index('shrey'))  # Finding the index of 'shrey'
print(user_list)  # Final state of the list