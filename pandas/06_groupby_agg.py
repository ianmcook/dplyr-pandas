# # Grouping and aggregating data in a pandas DataFrame

# Import modules and read games data
import numpy as np
import pandas as pd
games = pd.read_table('data/games/games.csv', sep=',')
games


# ## Aggregation with grouping

# To aggregate the data in a pandas DataFrame by
# group, use the `groupby` method immediately 
# followed by the `agg` method:

games \
  .groupby('min_age') \
  .agg(avg_list_price=('list_price','mean'))
  
# Load the flights dataset to demonstrate on larger data
flights = pd.read_csv('data/flights/flights.csv')

# You can specify muliple grouping columns in a list,
# and you can return multiple aggregates:
flights \
  .groupby(['origin', 'month']) \
  .agg(
    n=('flight','size'), \
    min_arr_delay=('arr_delay','min'), \
    max_arr_delay=('arr_delay','max'), \
    avg_arr_delay=('arr_delay','mean') \
  )


# ## Aggregation without grouping

# pandas expects a `groupby` before the `agg`. 
# To aggregate over the whole DataFrame without 
# any grouping, use a lambda in `groupby` to group 
# by a dummy column with constant value 0:

games \
  .groupby(lambda x: 0) \
  .agg(avg_list_price=('list_price','mean'))


# ## Grouping and aggregating missing values

# Load the inventory data (since the games data has no
# missing values)
inventory = pd.read_table('data/inventory/data.txt')
inventory

# The function `count` does not count missing values. To 
# count missing values, use `size`:

inventory \
  .groupby(lambda x: 0) \
  .agg( \
    num_total=('aisle','size'), \
    num_aisle_not_missing=('aisle','count') \
  )

inventory \
  .groupby('shop') \
  .agg( \
    num_total=('aisle','size'), \
    num_aisle_not_missing=('aisle','count') \
  )

# Aggregate functions ignore missing values
inventory \
  .groupby('shop') \
  .agg(avg_price=('price','mean'))

# With pandas, missing values in grouping columns
# are _not_ included in the results by default
inventory \
  .groupby('aisle') \
  .agg(num_rows=('aisle','size')) 

# To include missing values in grouping columns,
# set `dropna=False` in `groupby()`:
inventory \
  .groupby('aisle', dropna=False) \
  .agg(num_rows=('aisle','size'))


# ## Removing the MultiIndex

# When you use `groupby` and `agg`, the resulting
# DataFrame has a _MultiIndex_ (a hierarchical
# index). You can see this by looking at the header
# of the DataFrame returned by the above examples;
# notice how there are two header rows instead of
# the usual one.

# This MultiIndex can cause some methods to behave
# in unexpected ways. To remove it, use the
# `reset_index` method:

flights \
  .groupby(['origin', 'month']) \
  .agg(
    n=('flight','size'), \
    min_arr_delay=('arr_delay','min'), \
    max_arr_delay=('arr_delay','max'), \
    avg_arr_delay=('arr_delay','mean') \
  ) \
  .reset_index()


# ## Aggregation with older versions of pandas

# The aggregation syntax described above is 
# supported in pandas version 0.25.0 (released
# July 18, 2019) and higher. In earlier versions
# of pandas, a different technique was required.
# See the file `07_groupby_agg.py` from an
# [earlier version of this material](https://github.com/ianmcook/strata-eu-2019/blob/master/1_data_manipulation/pandas/07_groupby_agg.py)
# for details.
