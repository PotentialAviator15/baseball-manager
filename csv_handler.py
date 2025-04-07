import csv
import os

def load_players():
    players = []
    if not os.path.isfile('players.csv'):
        print("File not found: players.csv")
        return players
    with open('players.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) 
        for row in reader:
            players.append(row)
    return players

def save_players(players):
    with open('players.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Position", "AtBats", "Hits", "BattingAverage"])  
        writer.writerows(players)