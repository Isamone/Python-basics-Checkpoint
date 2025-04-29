while True :
    user_guess = int(input("Guess the secret number:"))
     
    if user_guess == secret_number:
        print("You are coreect!")
        break
    elif user_guess < secret_number:
      print("Too low! try again")
    else:
      print("Too high!")