# # Select specific columns from an R data frame using dplyr

# Load packages and read games data
library(readr)
games <- read_csv("data/games/games.csv")
games


# Load the dplyr package
library(dplyr)

# Use the dplyr verb `select()` to return a data frame
# (tibble) containing only some of the columns from the 
# `games` data frame
games %>% select(name, min_players, max_players)

# Write the expression on multiple lines
games %>% 
  select(name, min_players, max_players)
