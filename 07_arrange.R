# # Ordering rows in an R data frame

# Load packages and read games data
library(readr)
library(dplyr)
games <- read_csv("data/games/games.csv")
games


# Use the dplyr verb `arrange` to sort the rows of a data 
# frame
games %>% arrange(min_age)

# The default sort order is ascending. Use the helper 
# function `desc` to sort in descending order
games %>% arrange(desc(min_age))

# You can specify multiple columns to sort by
games %>% arrange(desc(max_players), min_age)

# After ordering rows, use the `head` function to limit
# the number of rows returned, to get the "top N" results
# For example: What are the two least expensive games?
games %>% 
  select(name, list_price) %>%
  arrange(list_price) %>%
  head(2)
