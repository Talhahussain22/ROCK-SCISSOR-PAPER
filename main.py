import random
import time
print("____________________________________________")
print("\t\tWelcome to ROCK PAPER SCISSORS")
print("____________________________________________")
ask=input("Do you want to play the game(Y/N):").upper()
if ask!='Y':
    quit()
user_wins=0
computer_wins=0
while True:
    l=['ROCK','PAPER','SCISSOR','Q']
    print("User's Turn!")
    user=input(f"Enter ROCK/PAPER/SCISSOR or Q for quit:").upper()
    if user not in l:
        print("User's Turn!")
        user = input(f"Enter ROCK/PAPER/SCISSOR or Q for quit:").upper()

    if user=='Q':
        break
    print("Computer's Turn!")
    time.sleep(0.5)
    computer=random.choice(l)
    print(computer)

    if user==computer:
        print("DRAW!")
    elif user=='ROCK':
        if computer=='PAPER':
            print("You have selected ROCK and computer has selected PAPER")
            print("COMPUTER WON!")
            computer_wins+=1
        elif computer=='SCISSOR':
            print("You have selected ROCK and computer has selected SCISSOR")
            print("YOU WON!")
            user_wins+=1

    elif user == 'PAPER':
        if computer == 'ROCK':
            print("You have selected PAPER and computer has selected ROCK")
            print("YOU WON!")
            user_wins+=1
        elif computer == 'SCISSOR':
            print("You have selected PAPER and computer has selected SCISSOR")
            print("COMPUTER WON!")
            computer_wins+=1

    elif user == 'SCISSOR':
        if computer == 'PAPER':
            print("You have selected SCISSOR and computer has selected PAPER")
            print("YOU WON!")
            user_wins+=1
        elif computer == 'ROCK':
            print("You have selected SCISSOR and computer has selected ROCK")
            print("COMPUTER WON!")
            computer_wins+=1

print(f"You have won {user_wins} times!")
print(f'Computer has won {computer_wins} times!')


