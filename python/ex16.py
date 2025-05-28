from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")
