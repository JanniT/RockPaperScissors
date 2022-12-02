## Rock Paper Scissors -Game ##

import random
import menu
import choise

def main():
    print("\n\nRock, Paper, Scissors --- SHOOT!\n\n")

    while(1<2):
        choicesList = ['R', 'P', 'S']

        userChoise = choise.game()
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
        menuChoise = Menu.menu()
        if (menuChoise == 'Y') or (menuChoise == 'y'):
            main()
        if(menuChoise == 'N') or (menuChoise == 'n'):
            print("Thank you for playing!")
            return
        else: 
            print("Try again!\n")
            continue
    return None
main()