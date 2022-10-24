## Rock Paper Scissors -Game##

import random
from turtle import clear

def game():
    print("""Please choose a letter:
    'R' = Rock,
    'P' = Paper,
    'S' = Scissors\n""")

    choise = input("Choose your symbol: ")
    return choise

def menu(): 
    print("Do you want to play again? [Y] / [N]")
    menuChoise = input("[Y] / [N]: ")
    return menuChoise

def main():
    print("\n\nRock, Paper, Scissors --- SHOOT!\n\n")

    while(1<2):
        choicesList = ['R', 'P', 'S']

        userChoise = game()
        computerChoise = random.choices(choicesList)

        if (userChoise == "R" or userChoise == "P" or userChoise == "S"):
            print(f"  You chose '{userChoise}'")
            break

        else:
            print("\nTry again!\n")

    computerChoiseNew= (','.join(computerChoise))
    print(f"\nOpponent chose: {computerChoiseNew}\n")

    while(1<2): 

        if (userChoise == (computerChoiseNew)): 
            print("It's a tie!\n")
            break
        
        elif (computerChoiseNew == 'R' and userChoise == 'S'): 
            print("Scissors beats rock, computer wins!\n")
            break

        elif (computerChoiseNew == 'P' and userChoise == 'R'):
            print("Scissors beats rock, computer wins!\n")
            break

        elif (computerChoiseNew == 'S' and userChoise == 'P'):
            print("Scissors beats rock, computer wins!\n")
            break

        else: 
            print("You win!\n")
            break

    while(1<2):
        menuChoise = menu()
        if (menuChoise == 'Y'):
            main()
        if(menuChoise == 'N'):
            print("Thank you for playing!")
            return
        else: 
            print("Try again!\n")
            continue
    return None
main()