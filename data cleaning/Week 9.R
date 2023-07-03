read.csv(file = "/Users/shabbirkapadia/Downloads/data/inflammation-01.csv", header = FALSE)
weight_kg <- 55
weight_kg

# weight in pounds:
2.2 * weight_kg

weight_kg <- 57.5
# weight in kilograms is now
weight_kg

weight_lb <- 2.2 * weight_kg
# weight in kg...
weight_kg

# ...and in pounds
weight_lb

weight_kg <- 100.0
# weight in kg now...
weight_kg

# ...and weight in pounds still
weight_lb

dat <- read.csv(file = "/Users/shabbirkapadia/Downloads/data/inflammation-01.csv", header = FALSE)
head(dat)

# Manipulating Data
class(dat)
dim(dat)
# first value in dat, row 1, column 1
dat[1, 1]
# middle value in dat, row 30, column 20
dat[30, 20]
dat[c(1, 3, 5), c(10, 20)]
1:5
3:12
dat[1:4, 1:10]
dat[5:10, 1:10]
# All columns from row 5
dat[5, ]
# All rows from column 16-18
dat[, 16:18]

# first row, all of the columns
patient_1 <- dat[1, ]
# max inflammation for patient 1
max(patient_1)
# max inflammation for patient 2
max(dat[2, ])
# minimum inflammation on day 7
min(dat[, 7])
# mean inflammation on day 7
mean(dat[, 7])
# median inflammation on day 7
median(dat[, 7])
# standard deviation of inflammation on day 7
sd(dat[, 7])
# Summarize function
summary(dat[, 1:4])
avg_patient_inflammation <- apply(dat, 1, mean)
avg_day_inflammation <- apply(dat, 2, mean)

#Subsetting Data
animal <- c("m", "o", "n", "k", "e", "y")
# first three characters
animal[1:3]
# last three characters
animal[4:6]

#If the first four characters are selected using the subset animal[1:4], how can we obtain the first four characters in reverse order?
animal[4:1]  
#What is animal[-1]? What is animal[-4]? Given those answers, explain what animal[-1:-4] does.
#"o" "n" "k" "e" "y" and "m" "o" "n" "e" "y", which means that a single - removes the element at the given index position. animal[-1:-4] remove the subset, returning "e" "y", which is equivalent to animal[5:6].

#Use a subset of animal to create a new character vector that spells the word “eon”, i.e. c("e", "o", "n").
animal[c(5,2,3)]

#SUBSETTING AND RE-ASSIGNMENT
whichPatients <- seq(2, 60, 2) # i.e., which rows
whichDays <- seq(1, 5)         # i.e., which columns
dat2 <- dat
# check the size of your subset: returns `30 5`, that is 30 [rows=patients] by 5 [columns=days]
dim(dat2[whichPatients, whichDays])
dat2[whichPatients, whichDays] <- dat2[whichPatients, whichDays] / 2
dat2

#Plotting
plot(avg_day_inflammation)

max_day_inflammation <- apply(dat, 2, max)
plot(max_day_inflammation)

min_day_inflammation <- apply(dat, 2, min)
plot(min_day_inflammation)

#Defining Function
fahrenheit_to_celsius <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  return(temp_C)
}
fahrenheit_to_celsius(32)
celsius_to_kelvin <- function(temp_C) {
  temp_K <- temp_C + 273.15
  return(temp_K)
}
celsius_to_kelvin(0)

fahrenheit_to_kelvin <- function(temp_F) {
  temp_C <- fahrenheit_to_celsius(temp_F)
  temp_K <- celsius_to_kelvin(temp_C)
  return(temp_K)
}
# freezing point of water in Kelvin
fahrenheit_to_kelvin(32.0)

# freezing point of water in Fahrenheit
celsius_to_kelvin(fahrenheit_to_celsius(32.0))

#Functions to create graphs
analyze <- function(filename) {
  # Plots the average, min, and max inflammation over time.
  # Input is character string of a csv file.
  dat <- read.csv(file = filename, header = FALSE)
  avg_day_inflammation <- apply(dat, 2, mean)
  plot(avg_day_inflammation)
  max_day_inflammation <- apply(dat, 2, max)
  plot(max_day_inflammation)
  min_day_inflammation <- apply(dat, 2, min)
  plot(min_day_inflammation)
}

#A FUNCTION WITH DEFAULT ARGUMENT VALUES
rescale <- function(v, lower = 0, upper = 1) {
  # Rescales a vector, v, to lie in the range lower to upper.
  L <- min(v)
  H <- max(v)
  result <- (v - L) / (H - L) * (upper - lower) + lower
  return(result)
}

#Analyzing multiple data sets
analyze <- function(filename) {
  # Plots the average, min, and max inflammation over time.
  # Input is character string of a csv file.
  dat <- read.csv(file = filename, header = FALSE)
  avg_day_inflammation <- apply(dat, 2, mean)
  plot(avg_day_inflammation)
  max_day_inflammation <- apply(dat, 2, max)
  plot(max_day_inflammation)
  min_day_inflammation <- apply(dat, 2, min)
  plot(min_day_inflammation)
}

analyze("/Users/shabbirkapadia/Downloads/data/inflammation-01.csv")
analyze("/Users/shabbirkapadia/Downloads/data/inflammation-02.csv")

#For Loops
best_practice <- c("Let", "the", "computer", "do", "the", "work")
print_words <- function(sentence) {
  print(sentence[1])
  print(sentence[2])
  print(sentence[3])
  print(sentence[4])
  print(sentence[5])
  print(sentence[6])
}

print_words(best_practice)
best_practice[-6]
print_words(best_practice[-6])

print_words <- function(sentence) {
  for (word in sentence) {
    print(word)
  }
}

print_words(best_practice)

#Summing Values
ex_vec <- c(4, 8, 15, 16, 23, 42)
sum(ex_vec)

#Processing Multiple Files
list.files(path = "/Users/shabbirkapadia/Downloads/data", pattern = "inflammation")

filenames <- list.files(path = "/Users/shabbirkapadia/Downloads/data",  
                        # Now follows a regular expression that matches:
                        pattern = "inflammation-[0-9]{2}.csv",
                        #          |            |        the standard file extension of comma-separated values
                        #          |            the variable parts (two digits, each between 0 and 9)
                        #          the static part of the filenames
                        full.names = TRUE)
filenames <- filenames[1:3]
for (f in filenames) {
  print(f)
  analyze(f)
}