secretnum = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess == secretnum:
        print("You won ..")
        break
else:
        print("Try again")