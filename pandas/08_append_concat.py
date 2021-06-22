# # Combining pandas DataFrames by row

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games

# Create a second DataFrame describing more games
more_games = pd.DataFrame(
  [[6, 'Checkers', None, -3000, 6, 2, 2, 8.99 ],
   [7, 'Chess',    None,  500,  8, 2, 2, 12.99]],
  columns=['id', 'name', 'inventor', 'year', 'min_age', 'min_players', 'max_players', 'list_price']
)
more_games

# Use the DataFrame method `append` to combine two
# DataFrames vertically, adding the rows of the second
# at the bottom of the first. This is equivalent to
# what the SQL operator `UNION ALL` does
games.append(more_games)


# To remove duplicates from the combined result, like 
# the SQL operator `UNION DISTINCT` does, use the
# DataFrame method `drop_duplicates` after combining 
# the DataFrames. For example, the following series of 
# operations combines the `games` and `more_games` 
# DataFrames, selects only the `min_players` and 
# `max_players` columns, and returns only the distinct 
# (unique) rows (the rows with unique combinations of 
# `min_players` and `max_players`).
games \
  .append(more_games) \
  .filter(['min_players', 'max_players']) \
  .drop_duplicates()


# # Combining pandas DataFrames by column

# Create a second DataFrame with more columns
# describing the games in the `games` DataFrame
more_columns = pd.DataFrame(
  [[2, False],
   [0, False],
   [2, False],
   [0, True],
   [5, False]],
  columns=['dice', 'spinner']
)
more_columns

# Use the pandas function `concat` with `axis=1` to
# combine two or more DataFrames horizontally, adding
# the columns of the second to the right of the first 
pd.concat([games, more_columns], axis=1)
