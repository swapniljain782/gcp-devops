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

line1 = input("line 1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()