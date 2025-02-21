def main():
    print("=" * 63)
    print("Baseball Team Manager")
    print("This program calculates the batting average for a player based")
    print("on the player's official number of at bats and hits.")
    print("=" * 63)
    
    # Get input from the user
    name = input("Player's name: ")
    at_bats = int(input("Official number of at bats: "))
    hits = int(input("Number of hits: "))
    
    # Calculate the batting average
    if at_bats > 0:
        batting_average = hits / at_bats
    else:
        batting_average = 0.0
    
    # Display the results
    print(f"\n{name}'s batting average is {batting_average:.3f}")


main()

