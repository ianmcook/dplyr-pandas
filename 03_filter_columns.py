# # Select specific columns from a pandas DataFrame

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games


# Use the DataFrame method `filter` to return a DataFrame 
# containing only some of the columns from the `games` 
# DataFrame
games.filter(['name', 'min_players', 'max_players'])


# Write the expression on multiple lines
games \
  .filter(['name', 'min_players', 'max_players'])

# or

(games
  .filter(['name', 'min_players', 'max_players']))


# Alternatively, use the `.loc` indexer:
games \
  .loc[:, ['name', 'min_players', 'max_players']]
