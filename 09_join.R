# # Joining R data frames

# Load packages
library(readr)
library(dplyr)

# Read employees data
employees <- read_tsv("data/employees/employees.txt")
employees

# Read offices data
offices <- read_tsv("data/offices/offices.txt")
offices


# dplyr provides several _two-table verbs_ that can be 
# used to join two data frames together. These include:
# - `inner_join()` for inner joins
# - `left_join()` for left outer joins
# - `right_join()` for right outer joins
# - `full_join()` for full outer joins

# For example, use `left_join()` to perform a left outer
# join on the `employees` and `offices` data frames
employees %>% left_join(offices)

# dplyr automatically identifies common column names in
# the two data frames and joins on them. To manually
# specify the join key columns, use the `by` argument
employees %>% left_join(offices, by = "office_id")

# For more details, see the dplyr `join` help page:
?join