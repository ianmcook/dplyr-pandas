# # Inspect a pandas DataFrame

# Import modules and read data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games


# How many rows and columns does the data have?
games.shape
games.shape[0]
games.shape[1]


# What are the names and data types of the columns?
games.dtypes
games.dtypes.index.values
games.dtypes.values
