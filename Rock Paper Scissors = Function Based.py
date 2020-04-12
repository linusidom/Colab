import random
# All imports should be done at the top of the file
# and be done outside of any loops or conditi

while True: 

    options = ['rock', 'paper', 'scissors']
    choice = input('Enter your Choice: ')
    choice = choice.lower()

#all of the codes are from lessons except line 10-13
    # if choice not in options:
    #   print(input("Reenter your Choice: "))
    # else:
    #   continue

    # We can keep the player in the game with a while loop until they pick the right option
    # If they want to exit the program they can do that as well
    while choice not in options:
        choice = input("Reenter your Choice: ")
        choice = choice.lower()
        if choice == 'exit':
            print("Thank you for Playing")
            exit(1)
      
    computer = random.choice(options)

    if (choice == 'rock') and (computer == 'paper'):
        print('Computer Wins')
    elif (choice == 'rock') and (computer == 'scissors'):
        print('You Wins')
    elif (choice == 'scissors') and (computer == 'rock'):
        print('Computer Wins')
    elif (choice == 'scissors') and (computer == 'paper'):
        print('You Wins')
    elif (choice == 'paper') and (computer == 'scissors'):
        print('Computer Wins')
    elif (choice == 'paper') and (computer == 'paper'):
        print('You Wins')
    else:
        print("It's a tie")
