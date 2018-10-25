# # Ordering rows in a pandas DataFrame

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games

# Use the DataFrame method `sort_values` to sort the rows of
# a DataFrame
games.sort_values('min_age')

# The default sort order is ascending. Use the the parameter
# `ascending` to control the sort order
games.sort_values('min_age', ascending=False)

# You can specify multiple columns to sort by, in a list
# with the sort orders also specified in a list
games \
  .sort_values(
    ['max_players','min_age'],
    ascending=[False,True]
  )

# After ordering rows, use the `head` method to limit
# the number of rows returned, to get the "top N" results
# For example: What are the two least expensive games?
games \
  .filter(['name', 'list_price']) \
  .sort_values('list_price') \
  .head(2)
