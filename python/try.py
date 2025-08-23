while true:
    try:
       mark_input = input("Enter a mark: ")

       #check if input is a digit or negative integer
       if not mark_input.isdigit():
           raise ValueError("Please enter a valid interger number.")

       mark = int(mark_input)

       if mark > 100 or mark < 0:
           print("Invalid input/mark. Please enter a value between 0 and 100.")
       else:
        if mark >= 80:
            print("You got distinction")
        elif mark >= 60:
            print("You git first class")
        elif mark >= 40:
            print("You got second class")
        else:
            print("You got failed")
        break 
        # only break when valid input is provided
