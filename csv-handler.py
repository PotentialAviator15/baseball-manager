import csv

def load_players():
    players = []
    with open('players.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the title row
        for row in reader:
            players.append(row)
    return players

def save_players(players):
    with open('players.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Position", "AtBats", "Hits", "BattingAverage"])  # Write the title row
        writer.writerows(players)