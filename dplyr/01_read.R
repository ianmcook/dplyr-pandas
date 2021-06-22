# # Read data from a delimited text file into an R data frame

# Use the built-in R function `read.table()` to read data
# from a delimited text file into an R data frame
games <- read.table(
  "data/games/games.csv",
  header = TRUE,
  sep = ","
)

# The default delimiter for `read.table()` is any
# whitespace. Use the `sep` argument to specify a 
# different delimiter. By default, `read.table()`
# expects the file to have no header row. To treat the
# first row of the file as a header row containing the
# column names, specify `header = TRUE`

# For details about the `read.table()` function, run the
# help command:
?read.table

# Alternatively, use the `read.csv()` function which
# expects a comma delimiter and a header row by default
games <- read.csv("data/games/games.csv")

# These functions return a `data.frame` object
class(games)

# View the data
games


# Instead of using R's built-in functions for reading
# data, you can use the functions in the 
# [readr](https://readr.tidyverse.org) package. These
# functions behave slightly differently, and return
# ["tibble"](https://tibble.tidyverse.org) objects, which
# have class `tbl_df`. Tibbles are still data frames, but
# they have some different behaviors.

# Load the readr package
library(readr)

# Call the function `read_csv()` (underscore instead of
# dot) to read data from a comma-delimited file into a 
# tibble.
games <- read_csv("data/games/games.csv")

# These functions return a `tbl_df` object, which also
# inherits class `data.frame`
class(games)

# View the data as a tibble
games

# View the data as a data frame
as.data.frame(games)
