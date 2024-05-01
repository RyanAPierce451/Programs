"""
************
PROGRAMMER: RYAN A PIERCE
DATE:   FEBRUARY 24, 2023
ASSIGNMENT:  HOMEWORK #4: FRIENDLY GAME WITH FRIENDS
ALGORITHM:  READS A TEXT FILE OF GAME TILES (A-Z) AND A CROSSWORD FILE AND  CREATES 4 GROUPS OF RANDOM LETTERS FROM THE GAME TILES FILE AND FINDS ALL THE COMBINATIONS OF WORDS AVAILABLE AND ALSO PROVIDES A POINT RATING FROM PICKLED DATA FOR EACH WORD
************
"""
import random
import pickle

# Function to print scores of a player's words
def printScores(x):
    # Initializes player's score and count of words played
    player_score = 0
    count = 0
    # Iterates through each word played by the player
    for i in range(len(x)):
        count += 1
        # Prints the word and its score
        print(f"{count}: {x[i]} - {points[i]} points")
        # Adds the score of the word to the player's total score
        player_score += points[i]
    # Prints the player's total score     
    print(f'Total Score: {player_score}')
    return int(player_score)

            
        

# Function to find all words that can be formed from the player's hand
def MatchingWords(Player):
    global points
    points = []
    words = []
    # Iterates through each word in the crossword list
    for word in crossword_list:
        check = True
        list_letters = list(Player)
        # Iterates through each letter in the word
        for letter in word:
            # If the letter is not in the player's hand, break and check the next word
            if letter not in list_letters:
                check = False
                break
            # If the letter is in the player's hand, remove it from the list of letters
            else:
               list_letters.remove(letter)
        # If all letters in the word are in the player's hand, add the word to the list of words
        if check:
            words.append(word)
            point = 0
            # Calculates the score of the word by summing the scores of each letter in the word
            for letter in word:
                if letter in scores:
                    point += scores[str(letter)] 
            # Adds the score of the word to the list of points
            points.append(point)                
    return words

# Function to deal tiles to each player
def deal_tiles(player_count):
    players = player_count
    count = player_count * 8
    while count > 0:
        # Deals tiles to Player 1
        if player_count >= 1:
            key = random.choice(list(game_tiles_dict.keys()))
            while True:
                if game_tiles_dict[str(key)] > 0:
                    Player1.append(str(key).lower())
                    game_tiles_dict[str(key)] -= 1
                    break
                key = random.choice(list(game_tiles_dict.keys()))
            count -= 1

        # Deals tiles to Player 2
        if player_count >= 2:
            key = random.choice(list(game_tiles_dict.keys()))
            while True:
                if game_tiles_dict[str(key)] > 0:
                    Player2.append(str(key).lower())
                    game_tiles_dict[str(key)] -= 1
                    break
                key = random.choice(list(game_tiles_dict.keys()))
            count -= 1

        # Deals tiles to Player 3
        if player_count >= 3:
            key = random.choice(list(game_tiles_dict.keys()))
            while True:
                if game_tiles_dict[str(key)] > 0:
                    Player3.append(str(key).lower())
                    game_tiles_dict[str(key)] -= 1
                    break
                key = random.choice(list(game_tiles_dict.keys()))
            count -= 1

        # Deals tiles to Player 4
        if player_count >= 4:
            key = random.choice(list(game_tiles_dict.keys()))
            while True:
                if game_tiles_dict[str(key)] > 0:
                    Player4.append(str(key).lower())
                    game_tiles_dict[str(key)] -= 1
                    break
                key = random.choice(list(game_tiles_dict.keys()))
            count -= 1

# Initializes file names and necessary lists and dictionaries
crossword_file = 'CROSSWD.TXT' 
game_file = 'GameTiles.txt'
crossword_list = []
game_tiles_dict = {}
scores = {}
Player1 = []
Player2 = []
Player3 = []
Player4 = []
playerscore1 = 0
playerscore2 = 0
playerscore3 = 0
playerscore4 = 0
all_players_scores = []
winners = []

# Loads the tile scores from a binary file using pickle
file = open('tile_scores.dat', 'rb')
scores = pickle.load(file)
file.close()

# Reads the crossword and game tile files, and store the information in the appropriate lists and dictionaries
with open(crossword_file) as file:
    crossword = file.readlines()
    for i in range(0, len(crossword)):
        crss = str(crossword[i].strip())
        crossword_list.append(crss)

with open(game_file) as file:
    for i in file:
        (key, val) = i.split(',')
        game_tiles_dict[str(key).strip()] = int(val)

# Asks the user for the number of players, and validates the input
while True:
    player_count = int(input("How many players are playing: [Enter Number 1 - 4]: "))
    if player_count <= 4 and player_count >= 1:
        break
    else:
        print("Incorrect Player Count. Enter Again")

# Deals the tiles to the players based on the number of players        
deal_tiles(player_count)

# For each player, print their hand, calculate the scores of their words, and store their score in a list
if player_count >= 1:
    Player1S = "".join(str(letters) for letters in Player1)
    print("Word Scores and Words")
    print(f"Player 1's hand: {Player1S}")
    playerscore1 = printScores(MatchingWords(Player1))
    all_players_scores.append(playerscore1)
    print()
if player_count >= 2:
    Player2S = "".join(str(letters) for letters in Player2)
    print("Word Scores and Words")
    print(f"Player 2's hand: {Player2S}")
    playerscore2 = printScores(MatchingWords(Player2))
    all_players_scores.append(playerscore2)
    print()
if player_count >= 3:
    Player3S = "".join(str(letters) for letters in Player3)
    print("Word Scores and Words")
    print(f"Player 3's hand: {Player3S}")
    playerscore3 = printScores(MatchingWords(Player3))
    all_players_scores.append(playerscore3)
    print()
if player_count >= 4:
    Player4S = "".join(str(letters) for letters in Player4)
    print("Word Scores and Words")
    print(f"Player 4's hand: {Player4S}")
    playerscore4 = printScores(MatchingWords(Player4))
    all_players_scores.append(playerscore4)

#  Prints the scores of all players, and determine the winner(s)
print()
print(f"Scores: {all_players_scores}")
win = max(all_players_scores)
for i in range(len(all_players_scores)):
    if(all_players_scores[i] == win):
        winners.append(i+1)
print(f"Winner is: Player/Players: {winners}\nCongratulations!")