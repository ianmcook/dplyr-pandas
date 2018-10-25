# # Grouping and aggregating data in a pandas DataFrame

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games


# ## Aggregation without grouping

# Use the DataFrame method `agg` to reduce all rows of 
# a table down to a single row by aggregating the
# specified column by the specified function

# As the argument to `agg`, pass a dictionary in the form  
# `{'column_name': ['aggregate_function']}`
games \
  .agg({'list_price': ['mean']})


# You can also specify multiple aggregate functions in a list
# but this transposes the result. You can transpose it back
# using the `transpose` method
games \
  .agg({'min_age': ['count', 'nunique']}) \
  .transpose()


# The `agg` method does not give you control over the
# column names in the aggregated result, but you can use
# `rename` to rename them
games \
  .agg({'list_price': ['mean']}) \
  .rename(columns = {'list_price': 'avg_list_price'})

games \
  .agg({'min_age': ['count', 'nunique']}) \
  .transpose() \
  .rename(
    columns = {
      'count': 'count_min_age',
      'nunique': 'unique_count_min_age'
    }
  )
  

# ## Aggregation with grouping

# Use the DataFrame method `groupby` immediately before
# `agg` to aggregate by groups
games \
  .groupby('min_age') \
  .agg({'list_price': ['mean']})

  
# Load the flights dataset to demonstrate on larger data
flights = pd.read_csv('data/flights/flights.csv')

# You can specify muliple grouping columns in a list
flights \
  .groupby(['origin', 'month']) \
  .agg({'arr_delay': ['count', 'min', 'max', 'mean']})

# When you use grouping, the result is not transposed.


# ## Grouping and aggregating missing values

# Load the inventory data (since the games data has no
# missing values)
inventory = pd.read_table('data/inventory/data.txt')
inventory

# The function `count` does not count missing values. To 
# count missing values, use `len`. Because `len` is a 
# funcion defined in the Python language, not in the 
# pandas package, do not enclose it in quotes:
inventory \
  .agg({'aisle': [len, 'count']}) \
  .transpose()

inventory \
  .groupby('shop') \
  .agg({'aisle': [len, 'count']}) 

# Aggregate functions ignore missing values
inventory \
  .groupby('shop') \
  .agg({'price': ['mean']})

# With pandas, missing values in grouping columns are not
# included in the results
inventory \
  .groupby('aisle') \
  .agg({'aisle': [len]}) 
