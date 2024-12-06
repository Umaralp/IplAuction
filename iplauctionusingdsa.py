# -*- coding: utf-8 -*-
"""IplAuction_UsingDSA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19nknU_A9F0PTQR1mM658Zhh7SJt-fzw2

# **IPL Auction Simulator: Team Budget Management and Player Acquisition**

The 'IplAuction_UsingDSA' Program simulates the process of IPL auction where teams bid for players based on their available budget. The data for players, including their name, nationality, type, and price paid, is imported from a CSV file (`IPL_PLAYERS.csv`).

The program defines **Player** and **Team** classes, where each player has attributes like **name, nationality, and price,** and each team manages a budget and a list of players. It uses a custom hash table to efficiently look up players during the auction. Teams take turns bidding on players, and if the team’s budget allows, the player is added to their squad. The program offers a **menu-driven interface** where users can conduct the auction, view team leaderboards, see the top and least expensive purchases, and search for players. Additionally, it tracks the performance of the hash table for debugging.bold text
"""

# Importing necessary libraries
from google.colab import files
import io
import pandas as pd
import hashlib
from collections import defaultdict

# Upload and load the dataset (IPL Players)
uploaded = files.upload()

# Load the dataset into a DataFrame from the uploaded CSV file
players_df = pd.read_csv(io.BytesIO(uploaded['IPL_PLAYERS.csv']))  # Use the correct filename from the uploaded dictionary

# Class to represent each player in the IPL auction
class Player:
    def __init__(self, name, nationality, player_type, price_paid, team=None):
        self.name = name
        self.nationality = nationality
        self.player_type = player_type
        self.price_paid = price_paid
        self.team = team

    def __repr__(self):
        return f'{self.name} ({self.team}) - {self.price_paid}'

# Class to represent an IPL team (budget, players, etc.)
class Team:
    def __init__(self, name, budget, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.budget = budget
        self.players = []  # Players in the team
        self.total_spent = 0  # Total money spent on players

    # Method to add a player to the team if the budget allows
    def add_player(self, player):
        if self.budget >= player.price_paid:
            self.players.append(player)
            self.total_spent += player.price_paid
            self.budget -= player.price_paid
            return True
        return False

    def __repr__(self):
        return f'Team: {self.name} ({self.abbreviation}), Budget Left: {self.budget}, Total Spent: {self.total_spent}, Players: {len(self.players)}'

# Class to represent the Hash Table (for storing players and searching by name)
class HashTable:
    def __init__(self, size=100, collision_strategy="chaining"):
        self.size = size
        self.table = [None] * size
        self.collision_strategy = collision_strategy
        if collision_strategy == "chaining":
            self.table = [defaultdict(list) for _ in range(size)]  # Using chaining with defaultdict

    def hash_function(self, key):
        # Using SHA-256 for hashing keys
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.size

    # Method to insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.collision_strategy == "chaining":
            self.table[index][key].append(value)
        elif self.collision_strategy == "open_addressing":
            while self.table[index] is not None:
                index = (index + 1) % self.size  # Linear probing for open addressing
            self.table[index] = (key, value)

    # Method to search for a key in the hash table
    def search(self, key):
        index = self.hash_function(key)
        if self.collision_strategy == "chaining":
            return self.table[index].get(key, [])  # Search in the chain for the key
        elif self.collision_strategy == "open_addressing":
            original_index = index
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    return self.table[index][1]
                index = (index + 1) % self.size
                if index == original_index:
                    break  # Avoid infinite loop
        return None

    def __repr__(self):
        # Represent the hash table for debugging
        result = []
        for i, bucket in enumerate(self.table):
            if self.collision_strategy == "chaining":
                if bucket:  # Only include non-empty chains
                    result.append(f"Index {i}: {dict(bucket)}")
            else:
                if bucket is not None:  # For open addressing, include the value if not None
                    result.append(f"Index {i}: {bucket}")
        return "\n".join(result) if result else "Hash Table is empty."

# Function to create a list of Player objects from the dataset
def create_auction_heap(players_df):
    players = []
    for _, row in players_df.iterrows():
        price_paid = int(row['PRICE PAID'])  # Ensure 'PRICE PAID' is correctly formatted in the CSV
        player = Player(row['PLAYERS'], row['NATIONALITY'], row['TYPE'], price_paid)
        players.append(player)
    return players

# Function to create a list of Team objects
def create_teams():
    return [
        Team("Mumbai Indians", 100000000, "MI"),
        Team("Sunrisers Hyderabad", 100000000, "SRH"),
        Team("Kolkata Knight Riders", 100000000, "KKR"),
        Team("Royal Challengers Bengaluru", 100000000, "RCB"),
        Team("Rajasthan Royals", 100000000, "RR"),
        Team("Punjab Kings", 100000000, "PBKS"),
        Team("Delhi Capitals", 100000000, "DC"),
        Team("Gujarat Titans", 100000000, "GT"),
        Team("Lucknow Super Giants", 100000000, "LSG"),
        Team("Chennai Super Kings", 100000000, "CSK")
    ]

# Function to conduct the auction by sequentially offering players to teams
def conduct_auction_sequential(players_list, teams):
    team_index = 0
    for player in players_list:
        team = teams[team_index]
        if team.add_player(player):
            player.team = team.abbreviation  # Assign the team to the player
            print(f"{player.name} sold to {team.name} ({team.abbreviation}) for {player.price_paid}")
        else:
            print(f"{player.name} remains unsold due to budget constraints.")
        team_index = (team_index + 1) % len(teams)  # Cycle through the teams

# Function to sort the teams by total spending
def sort_teams_by_spending(teams):
    return sorted(teams, key=lambda x: sum(player.price_paid for player in x.players), reverse=True)

# Function to display the leaderboard of teams after the auction
def display_leaderboard(teams_sorted):
    print("\nLeaderboard after Auction:")
    for team in teams_sorted:
        print(team)

# Function to display the top 10 most expensive purchases
def display_top_purchases(players_list):
    top_purchases = sorted(players_list, key=lambda x: x.price_paid, reverse=True)[:10]
    print("\nTop Purchases of 2024 IPL:")
    for player in top_purchases:
        print(f"{player.name} ({player.nationality}, {player.player_type}) - {player.price_paid}")

# Function to display the least expensive purchases
def display_least_expensive_purchases(players_list):
    least_expensive = sorted(players_list, key=lambda x: x.price_paid)[:10]
    print("\nLeast Expensive Purchases of 2024 IPL:")
    for player in least_expensive:
        print(f"{player.name} ({player.nationality}, {player.player_type}) - {player.price_paid}")

# Menu-driven main program
if __name__ == "__main__":
    # Create list of players and teams
    players_list = create_auction_heap(players_df)
    teams = create_teams()
    auction_conducted = False

    # Initialize a hash table for players (to quickly search by name)
    hash_table = HashTable(size=100, collision_strategy="chaining")
    for player in players_list:
        hash_table.insert(player.name, player)

    # Main loop to interact with the user and perform actions
    while True:
        print("\n--- IPL Auction Menu ---")
        print("1. Conduct Auction")
        print("2. Display Leaderboard")
        print("3. Display Top Purchases of 2024 IPL")
        print("4. Display Least Expensive Purchases")
        print("5. Search Player by Name")
        print("6. Show Hash Table Performance")
        print("7. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-7): ")

        # Perform the action based on user input
        if choice == "1":
            if not auction_conducted:
                print("\nConducting Auction...")
                conduct_auction_sequential(players_list, teams)
                auction_conducted = True
            else:
                print("Auction has already been conducted!")

        elif choice == "2":
            if auction_conducted:
                print("\nDisplaying Leaderboard...")
                teams_sorted = sort_teams_by_spending(teams)
                display_leaderboard(teams_sorted)
            else:
                print("Please conduct the auction first!")

        elif choice == "3":
            print("\nDisplaying Top Purchases...")
            display_top_purchases(players_list)

        elif choice == "4":
            print("\nDisplaying Least Expensive Purchases...")
            display_least_expensive_purchases(players_list)

        elif choice == "5":
            player_name = input("Enter player name to search: ")
            result = hash_table.search(player_name)
            if result:
                print(f"Player Found: {result}")
            else:
                print("Player not found.")

        elif choice == "6":
            print("Hash Table State:")
            print(hash_table)

        elif choice == "7":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")