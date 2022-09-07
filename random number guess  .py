actual_number = 165
attempts = 0

# user will get maximum score when he guessesd the number in first attempts.
# maximum score: 100

while True:
    attempts += 1        # attempts increment by one
           
    guess = int(input("guess the number between 100 and 200:\n"))

    if guess < actual_number:
        print('your number was small')

    elif guess > actual_number:
        print(' your number was high')

    else:
        print(f'you guessed the number in {attempts} attempts') # count the number of attempts in which user will guess the number.
        print(' your score: ',101-attempts)

        break
        
print('thanks for playing\nhave a good day!')

input("press  enter to exit")
