choice = ""
while choice != "8":
    print("Guess the number")
    choice = input("Enter your guess: ")

    if choice > "8":
        print("Your guess is too high.")
    elif choice < "8":
        print("Your guess is too low.")
    else:
        print("Yes!! You guess the correct number.")
