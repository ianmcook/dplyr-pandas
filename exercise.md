Complete the following exercises by chaining together
pandas DataFrame methods or dplyr verbs. Use the flights
data, in the file `data/flights/flights.csv`.

1. Find the five worst delayed destinations (largest 
   average arrival delay) for flights departing EWR. 
   Include the number of flights and the average
   arrival delay.

2. Calculate the average air speed of each flight in 
   units of miles per hour (`distance / air_time * 60`) 
   rounded to the nearest integer. Return a result set
   that includes the carrier, flight, origin, and dest
   columns, as well as the new column giving the air 
   speed, sorted in descending order of air speed. 
   Remove records with missing distance or air_time.
   What is the fastest flight in the data? The slowest?

3. Which airline's flights had the fastest average speed?

4. Which of the airlines that have at least 10,000
   flights in the dataset had the fastest average speed?
