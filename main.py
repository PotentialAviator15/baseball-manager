from csv_handler import load_players, save_players

positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def calculate(name, hits, at_bats):
    batting_average = hits / at_bats if at_bats > 0 else 0.0
    return round(batting_average, 3)

def menu():
    print("=" * 63)
    print("Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print(" ".join(positions))
    print("=" * 63)

def display_lineup():
    players = load_players()
    print(f"{'':<3}{'Player':<10}{'POS':<8}{'AB':<8}{'H':<8}{'AVG':<8}")
    print("-" * 55)
    for idx, player in enumerate(players, start=1):
        print(f"{idx:<3}{player[0]:<10}{player[1]:<8}{player[2]:<8}{player[3]:<8}{player[4]:<8}")

def add():
    players = load_players()
    name = input("Player's name: ")
    at_bats = int(input("Official number of at-bats: "))
    if at_bats < 0:
        print("At-bats cannot be negative. Exiting program.")
        return
    hits = int(input("Number of hits: "))
    if hits < 0:
        print("Invalid number of hits. Exiting program.")
        return
    elif hits > at_bats:
        print("Hits cannot be greater than at-bats. Exiting program.")
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
    player_number = int(input("Enter the player number to remove: "))
    if 1 <= player_number <= len(players):
        removed_player = players.pop(player_number - 1)
        save_players(players)
        print(f"{removed_player[0]} was removed.")
    else:
        print("Invalid player number. Please try again.")

def move():
    players = load_players()
    display_lineup()
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

def editstats():
    players = load_players()
    display_lineup()
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

def editpos():
    players = load_players()
    display_lineup()
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

def main():
    while True:
        menu()
        menu_option = int(input("Menu option:  "))
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
            print("Invalid option. Please choose a valid menu option.")

main()