# # Inspect an R data frame or tibble

# Load packages and read data
library(readr)
games <- read_csv("data/games/games.csv")
games


# How many rows and columns does the data have?
dim(games)
ncol(games)
nrow(games)


# What are the names and data types of the columns?
games # Read from top rows of tibble
colnames(games)
sapply(games, class)
