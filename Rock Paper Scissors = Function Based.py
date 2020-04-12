while True: 
    import random

    options = ['rock', 'paper', 'scissors']
    choice = input('Enter your Choice: ')
    choice = choice.lower()

#all of the codes are from lessons except line 10-13
    if choice not in options:
      print(input("Reenter your Choice: "))
    else:
      continue
      
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
