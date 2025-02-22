def calculate():
    name = input("Player's name: ") # get the player name
    at_bats = int(input("Official number of at bats: ")) # get the at_bats 
    hits = int(input("Number of hits: ")) # get the amount of hits 
    
    if at_bats > 0:
        batting_average = hits / at_bats
    else:
        batting_average = 0.0 
    
    print(f"\n{name}'s batting average is {batting_average:.3f}") # print the calculation to the terminal

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
    if not menuOption.isdigit():
        print("Menu options come in numbers, not letters. This isn't English class.")
        main()
        return  # exit function to prevent further execution, and to improve efficiency

    menuOption = int(menuOption)  # from here down it will work correctly for checking menu options

    if menuOption == 1:
        calculate()
    elif menuOption == 2:
        print("Bye!")
    else:
        print("Invalid option. Please choose a valid menu option.")
        main() # repeats the menu and the function, which allows for 

main()