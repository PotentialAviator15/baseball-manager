from csv_handler import load_players, save_players
import os

positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def calculate(hits, at_bats):
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

def load_players_as_dict():
    players_list = load_players()
    players = []
    for player in players_list:
        players.append({
            "name": player[0],
            "position": player[1],
            "at_bats": int(player[2]),
            "hits": int(player[3]),
            "average": player[4]
        })
    return players

def save_players_from_dict(players):
    players_list = []
    for player in players:
        players_list.append([
            player["name"],
            player["position"],
            player["at_bats"],
            player["hits"],
            player["average"]
        ])
    save_players(players_list)

def display_lineup():
    players = load_players_as_dict()
    print(f"{'':<3}{'Player':<10}{'POS':<8}{'AB':<8}{'H':<8}{'AVG':<8}")
    print("-" * 55)
    for idx, player in enumerate(players, start=1):
        print(f"{idx:<3}{player['name']:<10}{player['position']:<8}{player['at_bats']:<8}{player['hits']:<8}{player['average']:<8}")

def add():
    players = load_players_as_dict()
    name = input("Player's name: ")
    at_bats = input("Official number of at-bats: ")
    if not at_bats.isdigit() or int(at_bats) < 0:
        print("Invalid input. Please enter a non-negative number for at-bats.")
        return
    at_bats = int(at_bats)

    hits = input("Number of hits: ")
    if not hits.isdigit() or int(hits) < 0 or int(hits) > at_bats:
        print("Invalid input. Please enter a non-negative number for hits that is not greater than at-bats.")
        return
    hits = int(hits)

    playerpos = input("Position of the player: ")
    if playerpos not in positions:
        print(f"{playerpos} is not a valid position. Position names are case sensitive.")
        return

    batting_average = calculate(hits, at_bats)
    new_player = {
        "name": name,
        "position": playerpos,
        "at_bats": at_bats,
        "hits": hits,
        "average": batting_average
    }
    players.append(new_player)
    save_players_from_dict(players)
    print(f"{name} was added.")

def remove():
    players = load_players_as_dict()
    display_lineup()
    player_number = input("Enter the player number to remove: ")
    if not player_number.isdigit() or not (1 <= int(player_number) <= len(players)):
        print("Invalid input. Please enter a valid player number.")
        return
    player_number = int(player_number)
    removed_player = players.pop(player_number - 1)
    save_players_from_dict(players)
    print(f"{removed_player['name']} was removed.")

def move():
    players = load_players_as_dict()
    display_lineup()
    player_number = input("Enter the player number to move: ")
    if not player_number.isdigit() or not (1 <= int(player_number) <= len(players)):
        print("Invalid input. Please enter a valid player number.")
        return
    player_number = int(player_number)

    new_position = input("Enter the new position for the player: ")
    if not new_position.isdigit() or not (1 <= int(new_position) <= len(players)):
        print("Invalid input. Please enter a valid new position.")
        return
    new_position = int(new_position)

    player = players.pop(player_number - 1)
    players.insert(new_position - 1, player)
    save_players_from_dict(players)
    print(f"{player['name']} has been moved to position {new_position}.")

def editstats():
    players = load_players_as_dict()
    display_lineup()
    player_number = input("Enter the player number to edit stats: ")
    if not player_number.isdigit() or not (1 <= int(player_number) <= len(players)):
        print("Invalid input. Please enter a valid player number.")
        return
    player_number = int(player_number)

    at_bats = input("Enter the new number of at-bats: ")
    if not at_bats.isdigit() or int(at_bats) < 0:
        print("Invalid input. Please enter a non-negative number for at-bats.")
        return
    at_bats = int(at_bats)

    hits = input("Enter the new number of hits: ")
    if not hits.isdigit() or int(hits) < 0 or int(hits) > at_bats:
        print("Invalid input. Please enter a non-negative number for hits that is not greater than at-bats.")
        return
    hits = int(hits)

    players[player_number - 1]["at_bats"] = at_bats
    players[player_number - 1]["hits"] = hits
    players[player_number - 1]["average"] = calculate(hits, at_bats)
    save_players_from_dict(players)
    print(f"{players[player_number - 1]['name']}'s stats have been updated.")

def editpos():
    players = load_players_as_dict()
    display_lineup()
    player_number = input("Player number: ")
    if not player_number.isdigit() or not (1 <= int(player_number) <= len(players)):
        print("Invalid input. Please enter a valid player number.")
        return
    player_number = int(player_number)

    new_position = input("New player position: ")
    if new_position not in positions:
        print(f"{new_position} is not a valid position. Position names are case sensitive.")
        return

    players[player_number - 1]["position"] = new_position
    save_players_from_dict(players)
    print(f"{players[player_number - 1]['name']}'s position has been updated to {new_position}.")

def main():
    while True:
        menu()
        menu_option = input("Menu option: ")
        if not menu_option.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        menu_option = int(menu_option)
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