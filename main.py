from csv_handler import load_players, save_players
import os

positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def calculate(name, hits, at_bats):
    batting_average = hits / at_bats if at_bats > 0 else 0.0
    return f"{batting_average:.3f}"

def menu():
    print("=" * 63)
    print(f"{'Baseball Team Manager':^63}")
    print("=" * 63)
    print(f"{'MENU OPTIONS':^63}")
    print("1 - Display lineup".center(63))
    print("2 - Add player".center(63))
    print("3 - Remove player".center(63))
    print("4 - Move player".center(63))
    print("5 - Edit player position".center(63))
    print("6 - Edit player stats".center(63))
    print("7 - Exit program".center(63))
    print("\nPOSITIONS".center(63))
    print(" ".join(positions).center(63))
    print("=" * 63)
    if not os.path.isfile('players.csv'):
        print("Team data file could not be found.".center(63))
        print("You can create a new one if you want.".center(63))

def display_lineup():
    players = load_players()
    print(f"{'':<3}{'Player':<10}{'POS':<8}{'AB':<8}{'H':<8}{'AVG':<8}")
    print("-" * 55)
    for idx, player in enumerate(players, start=1):
        if len(player) == 5:  
            print(f"{idx:<3}{player[0]:<10}{player[1]:<8}{player[2]:<8}{player[3]:<8}{player[4]:<8}")
        else:
            print(f"Error: Player data is incomplete for player at index {idx}.")

def add():
    players = load_players()
    name = input("Player's name: ")
    try:
        at_bats = int(input("Official number of at-bats: "))
        if at_bats < 0:
            print("At-bats cannot be negative. Exiting program.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for at-bats. Exiting program.")
        return
    try:
        hits = int(input("Number of hits: "))
        if hits < 0:
            print("Invalid number of hits. Exiting program.")
            return
        elif hits > at_bats:
            print("Hits cannot be greater than at-bats. Exiting program.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for hits. Exiting program.")
        return
    playerpos = input("Position of the player: ")
    if playerpos not in positions:
        print(f"{playerpos} is not a valid position. Position names are case sensitive. Exiting the program.")
        return
    batting_average = calculate(name, hits, at_bats)
    new_player = [name, playerpos, at_bats, hits, batting_average]
    players.append(new_player)
    save_players(players)
    print(f"{name} was added.")

def remove():
    players = load_players()
    display_lineup()
    try:
        player_number = int(input("Enter the player number to remove: "))
        if 1 <= player_number <= len(players):
            removed_player = players.pop(player_number - 1)
            save_players(players)
            print(f"{removed_player[0]} was removed.")
        else:
            print("Invalid player number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def move():
    players = load_players()
    display_lineup()
    try:
        player_number = int(input("Enter the player number to move: "))
        if 1 <= player_number <= len(players):
            new_position = int(input("Enter the new position for the player: "))
            if 1 <= new_position <= len(players):
                player = players.pop(player_number - 1)
                players.insert(new_position - 1, player)
                save_players(players)
                print(f"{player[0]} has been moved to position {new_position}.")
            else:
                print("Invalid new position. Please try again.")
        else:
            print("Invalid player number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def editstats():
    players = load_players()
    display_lineup()
    try:
        player_number = int(input("Enter the player number to edit stats: "))
        if 1 <= player_number <= len(players):
            at_bats = int(input("Enter the new number of at-bats: "))
            if at_bats < 0:
                print("At-bats cannot be negative. Exiting function.")
                return
            hits = int(input("Enter the new number of hits: "))
            if hits < 0:
                print("Invalid number of hits. Exiting function.")
                return
            elif hits > at_bats:
                print("Hits cannot be greater than at-bats. Exiting function.")
                return
            players[player_number - 1][2] = at_bats
            players[player_number - 1][3] = hits
            players[player_number - 1][4] = calculate(players[player_number - 1][0], hits, at_bats)
            save_players(players)
            print(f"{players[player_number - 1][0]}'s stats have been updated.")
        else:
            print("Invalid player number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def editpos():
    players = load_players()
    display_lineup()
    try:
        player_number = int(input("Player number: "))
        if 1 <= player_number <= len(players):
            new_position = input("New player position: ")
            if new_position in positions:
                players[player_number - 1][1] = new_position
                save_players(players)
                print(f"{players[player_number - 1][0]}'s position has been updated to {new_position}.")
            else:
                print(f"{new_position} is not a valid position. Position names are case sensitive.")
        else:
            print("Invalid player number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        menu()
        try:
            menu_option = int(input("Menu option:  "))
        except ValueError:
            print("Not a valid option. Please try again.")
            continue
        if menu_option == 1:
            display_lineup()
        elif menu_option == 2:
            add()
        elif menu_option == 3:
            remove()
        elif menu_option == 4:
            move()
        elif menu_option == 5:
            editpos()
        elif menu_option == 6:
            editstats()
        elif menu_option == 7:
            print("Bye!")
            break
        else:
            print("Invalid option. Please choose a valid menu option. Restaring the program. \n\n\n\n\n\n\n\n\n\n\n")
            main()

main()