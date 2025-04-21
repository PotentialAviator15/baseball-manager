import os
from csv_handler import load_players, save_players


class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = int(at_bats)
        self.hits = int(hits)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        return f"{(self.hits / self.at_bats):.3f}" if self.at_bats > 0 else "0.000"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "average": self.batting_average,
        }

    @staticmethod
    def from_dict(data):
        return Player(
            data["first_name"],
            data["last_name"],
            data["position"],
            data["at_bats"],
            data["hits"],
        )


class BaseballManager:
    positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

    def __init__(self):
        self.players = self.load_players()

    def load_players(self):
        players_list = load_players()
        return [
            Player(
                first_name=row[0],
                last_name=row[1],
                position=row[2],
                at_bats=int(row[3]),
                hits=int(row[4]),
            )
            for row in players_list
        ]

    def save_players(self):
        players_list = [
            [
                player.first_name,
                player.last_name,
                player.position,
                player.at_bats,
                player.hits,
            ]
            for player in self.players
        ]
        save_players(players_list)

    def menu(self):
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
        print(" ".join(self.positions).center(63))
        print("=" * 63)
        if not os.path.isfile("players.csv"):
            print("Team data file could not be found.".center(63))
            print("You can create a new one if you want.".center(63))

    def display_lineup(self):
        print(f"{'':<3}{'Player':<20}{'POS':<8}{'AB':<8}{'H':<8}{'AVG':<8}")
        print("-" * 55)
        for idx, player in enumerate(self.players, start=1):
            print(
                f"{idx:<3}{player.full_name:<20}{player.position:<8}{player.at_bats:<8}{player.hits:<8}{player.batting_average:<8}"
            )

    def add_player(self):
        first_name = input("Player's first name: ")
        last_name = input("Player's last name: ")
        position = input("Position of the player: ")
        if position not in self.positions:
            print(f"{position} is not a valid position. Position names are case sensitive.")
            return
        at_bats = input("Official number of at-bats: ")
        if not at_bats.isdigit() or int(at_bats) < 0:
            print("Invalid input. Please enter a non-negative number for at-bats.")
            return
        hits = input("Number of hits: ")
        if not hits.isdigit() or int(hits) < 0 or int(hits) > int(at_bats):
            print("Invalid input. Please enter a non-negative number for hits that is not greater than at-bats.")
            return
        new_player = Player(first_name, last_name, position, int(at_bats), int(hits))
        self.players.append(new_player)
        self.save_players()
        print(f"{new_player.full_name} was added.")

    def remove_player(self):
        self.display_lineup()
        player_number = input("Enter the player number to remove: ")
        if not player_number.isdigit() or not (1 <= int(player_number) <= len(self.players)):
            print("Invalid input. Please enter a valid player number.")
            return
        player_number = int(player_number)
        removed_player = self.players.pop(player_number - 1)
        self.save_players()
        print(f"{removed_player.full_name} was removed.")

    def move_player(self):
        self.display_lineup()
        player_number = input("Enter the player number to move: ")
        if not player_number.isdigit() or not (1 <= int(player_number) <= len(self.players)):
            print("Invalid input. Please enter a valid player number.")
            return
        player_number = int(player_number)
        new_position = input("Enter the new position for the player: ")
        if not new_position.isdigit() or not (1 <= int(new_position) <= len(self.players)):
            print("Invalid input. Please enter a valid new position.")
            return
        new_position = int(new_position)
        player = self.players.pop(player_number - 1)
        self.players.insert(new_position - 1, player)
        self.save_players()
        print(f"{player.full_name} has been moved to position {new_position}.")

    def edit_player_stats(self):
        self.display_lineup()
        player_number = input("Enter the player number to edit stats: ")
        if not player_number.isdigit() or not (1 <= int(player_number) <= len(self.players)):
            print("Invalid input. Please enter a valid player number.")
            return
        player_number = int(player_number)
        player = self.players[player_number - 1]
        at_bats = input("Enter the new number of at-bats: ")
        if not at_bats.isdigit() or int(at_bats) < 0:
            print("Invalid input. Please enter a non-negative number for at-bats.")
            return
        hits = input("Enter the new number of hits: ")
        if not hits.isdigit() or int(hits) < 0 or int(hits) > int(at_bats):
            print("Invalid input. Please enter a non-negative number for hits that is not greater than at-bats.")
            return
        player.at_bats = int(at_bats)
        player.hits = int(hits)
        self.save_players()
        print(f"{player.full_name}'s stats have been updated.")

    def edit_player_position(self):
        self.display_lineup()
        player_number = input("Enter the player number to edit position: ")
        if not player_number.isdigit() or not (1 <= int(player_number) <= len(self.players)):
            print("Invalid input. Please enter a valid player number.")
            return
        player_number = int(player_number)
        player = self.players[player_number - 1]
        new_position = input("Enter the new position: ")
        if new_position not in self.positions:
            print(f"{new_position} is not a valid position. Position names are case sensitive.")
            return
        player.position = new_position
        self.save_players()
        print(f"{player.full_name}'s position has been updated to {new_position}.")

    def run(self):
        while True:
            self.menu()
            menu_option = input("Menu option: ")
            if not menu_option.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            menu_option = int(menu_option)
            if menu_option == 1:
                self.display_lineup()
            elif menu_option == 2:
                self.add_player()
            elif menu_option == 3:
                self.remove_player()
            elif menu_option == 4:
                self.move_player()
            elif menu_option == 5:
                self.edit_player_position()
            elif menu_option == 6:
                self.edit_player_stats()
            elif menu_option == 7:
                print("Bye!")
                break
            else:
                print("Invalid option. Please choose a valid menu option.")


if __name__ == "__main__":
    manager = BaseballManager()
    manager.run()