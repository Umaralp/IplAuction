# IPL Auction Simulator: Team Budget Management and Player Acquisition
## Overview
The IPL Auction Simulator is a program that mimics the process of an Indian Premier League (IPL) auction where teams bid for players to build their squads. The program allows users to manage team budgets, view top purchases, and conduct the auction in a sequential manner. Player data is imported from a CSV file containing player details such as name, nationality, type, and price paid. The program uses object-oriented programming to define Player and Team classes and employs a custom hash table to store and search players efficiently.

## Features
### Team and Player Management:
Teams have a defined budget and can bid on players.
Players have details like name, nationality, type, and price.
### Sequential Auction Process:
Players are auctioned off to teams in a rotating manner based on available budget.
### Hash Table Search:
Players are stored in a custom hash table for efficient searching by name.
### Leaderboard & Spending Overview:
After the auction, teams are ranked based on total spending, and top/least expensive purchases are displayed.
### Player Search:
Allows users to search for players by name.
### Menu-Driven Interface:
Users can interact with the program through a simple text-based menu.

## Installation
Clone or download the repository to your local machine.

Install Python (version 3.x recommended).

Install required libraries by running:


install pandas
Upload the CSV file containing player data when prompted in the program.

## Usage
Run the Python program to start the IPL Auction Simulator.
The program will prompt you with the following options:
Conduct Auction: Begin the auction and allow teams to bid on players.
Display Leaderboard: View the leaderboard, which shows each team's total spending and remaining budget.
Display Top Purchases: View the top 10 most expensive players purchased in the auction.
Display Least Expensive Purchases: View the top 10 least expensive players purchased in the auction.
Search Player by Name: Search for a player by their name and view their details.
Show Hash Table Performance: View the current state of the hash table.
Exit: Exit the program.

### Example Interaction 
--- IPL Auction Menu ---
1. Conduct Auction
2. Display Leaderboard
3. Display Top Purchases of 2024 IPL
4. Display Least Expensive Purchases
5. Search Player by Name
6. Show Hash Table Performance
7. Exit

Enter your choice (1-7): 1
Conducting Auction...

## Files
IPL_PLAYERS.csv: The CSV file containing player data. Ensure the file is uploaded in the correct format when prompted.
ipl_auction_simulator.py: The main Python file containing the program code.
## Contribution
Feel free to contribute to this project by submitting issues or pull requests. Contributions are welcome, and we encourage you to improve the auction simulation, add more features, or fix bugs.
