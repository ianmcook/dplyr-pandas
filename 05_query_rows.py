# # Returning a subset of rows from a pandas DataFrame

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games


# Use the DataFrame method `query` to return the subset
# of rows that satisfy some conditions

# The argument to `query` is a quoted string containing
# a Boolean expression. Bare column names can be used
# in the quoted string
games.query('min_age < 5')
games.query('5 <= max_players <= 6')

# To use a variable in the quoted string, use `@` before
# it
price_limit = 10.00
games.query('list_price <= @price_limit')

# You can use symbolic logical operators like `&` and `|`
# in the quoted string
games.query('list_price < 10 & max_players >= 6')


# You can use some `pandas.Series` methods and some 
# functions in the quoted string
games.query('name.isin(["Clue", "Risk"])')
games.query('name.isnull()')
games.query('name.str.startswith("C")')

# You can negate the truth of an expression using `not`
# or `~`:
games.query('not name.isin(["Clue", "Risk"])')
games.query('~name.str.startswith("C")')

# Some functions have negative versions
games.query('name.notnull()')


# To use an unsupported function, assign it to a variable
# and use `@` before the variable name in the expression
round = np.round
games.query('@round(list_price, 0) == 20')


# Alternatively, use the `.loc` indexer. To do this,
# you need to reference the original DataFrame or use
# a lambda
games.loc[games.min_age < 5, :]
games.loc[games.max_players.between(5,6), :]

games.loc[lambda x: x.min_age < 5, :]
games.loc[lambda x: x.max_players.between(5,6), :]
games.loc[lambda x: (x.list_price < 10) & (x.max_players >= 6), :]
games.loc[lambda x: ~x.name.isin(["Clue", "Risk"]), :]
games.loc[lambda x: ~x.name.str.startswith("C"), :]
