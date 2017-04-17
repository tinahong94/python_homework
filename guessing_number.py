from random import randint
random_number = randint(0, 9)

guess_number = None
total_guess = 1

while True:
    guess_number = int(input("Guess a number: "))

    if guess_number == "exit":
        break

    if guess_number < random_number:
        print ("The number you guess is too low")
    elif guess_number > random_number:
        print ("The number you guess is too high")
    else:
        print ("You guess the right number")
        print("Your guess number is " + str(guess_number))
        print("Your total guess is " + str(total_guess))
        break
    total_guess += 1


# print("Your guess number is " + str(guess_number))
# print("Your total guess is " + str(total_guess))

