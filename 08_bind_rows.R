# # Combining R data frames (adding rows)

# Load packages and read games data
library(readr)
library(dplyr)
games <- read_csv("data/games/games.csv")
games

# Create a second data frame describing more games
more_games <- tribble(
  ~id, ~name, ~inventor, ~year, ~min_age, ~min_players, ~max_players, ~list_price,
  6, 'Checkers', NA, -3000, 6, 2, 2,  8.99,
  7, 'Chess',    NA,   500, 8, 2, 2, 12.99
)
more_games


# Use the dplyr function `bind_rows()` to combine two
# data frames vertically, adding the rows of the second
# at the bottom of the first. This is equivalent to
# what the SQL operator `UNION ALL` does
games %>% bind_rows(more_games)


# To remove duplicates from the combined result, like 
# the SQL operator `UNION DISTINCT` does, use the dplyr
# function `distinct()` after combining the data frames.
# For example, the following series of operations
# combines the `games` and `more_games` data frames, 
# selects only the `min_players` and `max_players` 
# columns, and returns only the distinct (unique) rows 
# (the rows with unique combinations of `min_players`
# and `max_players`).
games %>% 
  bind_rows(more_games) %>%
  select(min_players, max_players) %>%
  distinct()
