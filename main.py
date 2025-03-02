def calculate(name, hits, at_bats):

    batting_average = hits / at_bats if at_bats > 0 else 0.0 ## ze math

    # Display the result
    print(f"\n{name}'s batting average is {batting_average:.3f}")

 # print the calculation to the terminal

def menu():
    print("=" * 63)
    print("Baseball Team Manager")
    print("This program calculates the batting average for a player based") 
    print("on the player's official number of at bats and hits.")
    print("1 - Calculate batting average")
    print("2 - Exit the program")
    print("=" * 63)

def main():
    menu()
    menuOption = input("Menu option:  ")
    # if its a letter input this clause will trigger down below, just further error handling
    # if not menuOption.isdigit():
    #     print("Menu options come in numbers, not letters. This isn't English class.")
    #     main()
    #     return  # exit function to prevent further execution, and to improve efficiency
    menuOption = int(menuOption)  # from here down it will work correctly for checking menu options
    if menuOption == 1:
        name = input("Player's name: ") 
        at_bats = int(input("Official number of at-bats: "))  ## the at bats input
        if at_bats < 0:
            print("At-bats cannot be negative. Exiting program.")
            return
        hits = int(input("Number of hits: "))  ## the hits input 
        if hits < 0:
            print("Invalid number of hits. Exiting program.")
            return
        if hits > at_bats:
            print("Hits cannot be greater than at-bats. Exiting program.")
            return
        calculate(name, hits, at_bats)
    elif menuOption == 2:
        print("Bye!")
    else:
        print("Invalid option. Please choose a valid menu option.")
        main() # function recursion

main()