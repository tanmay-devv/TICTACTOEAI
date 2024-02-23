import sys
import pandas as pd

# Load the game data from CSV
df = pd.read_csv("game_data.csv")

# Function to determine the next optimal move using minimax algorithm
def minimax(board, depth, is_maximizing):
    # Implement the minimax algorithm here
    pass

# Read game state from command-line arguments or from file
game_state = sys.argv[1]

# Determine the next optimal move using minimax algorithm
next_move = minimax(game_state, depth=3, is_maximizing=True)

# Print the next optimal move to stdout

print(str(next_move[0]) + " " + str(next_move[1]))