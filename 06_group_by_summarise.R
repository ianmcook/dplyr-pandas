# # Grouping and aggregating data in an R data frame

# Load packages and read games data
library(readr)
library(dplyr)
games <- read_csv("data/games/games.csv")
games


# ## Aggregation without grouping

# Use the dplyr verb `summarise` to reduce all rows of 
# a table down to a single row by aggregating the
# specified column by the specified function

games %>%
  summarise(avg_list_price = mean(list_price))

# dplyr defines a special aggregate function `n()` 
# that does not take any arguments. It returns the number of
# rows (like `COUNT(*)` in SQL)
games %>%
  summarise(
    count_min_age = n(),
    unique_count_min_age = n_distinct(min_age)
  )


# ## Aggregation with grouping

# Use the function `group_by()` immediately before
# `summarise` to aggregate by groups
games %>%
  group_by(min_age) %>%
  summarise(mean(list_price))

  
# Load the flights dataset to demonstrate on larger data
flights <- read_csv("data/flights/flights.csv")

# You can specify muliple grouping columns

# Aggregate functions in R do not ignore missing values;
# they return `NA` if any of the aggregated values are `NA`.
# Specify `na.rm = TRUE` to make them ignore missing values
flights %>%
  group_by(origin, month) %>%
  summarise(
    n = n(),
    min_arr_delay = min(arr_delay, na.rm = TRUE),
    max_arr_delay = max(arr_delay, na.rm = TRUE),
    avg_arr_delay = mean(arr_delay, na.rm = TRUE)
  )


# ## Grouping and aggregating missing values

# Load the inventory data (since the games data has no
# missing values)
inventory <- read_tsv("data/inventory/data.txt")
inventory

# To count the number of non-missing values, use an expression
inventory %>%
  summarise(
    num_total = n(),
    num_aisle_not_missing = sum(!is.na(aisle))
  )

# Use `na.rm = TRUE` to make aggregate functions ignore
# missing values
inventory %>%
  group_by(shop) %>%
  summarise(avg_price = mean(price))

inventory %>%
  group_by(shop) %>%
  summarise(avg_price = mean(price, na.rm = TRUE))

# With dplyr, missing values in grouping columns _are_
# included in the results
inventory %>%
  group_by(aisle) %>%
  summarise(n())
