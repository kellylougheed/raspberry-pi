#!/usr/bin/env python
# This program calculates whether a Martian year is a leap year
# A year is a leap year if it is odd or divisible by 10
# Initialize year variable
year = ""
# Program should loop until the user inputs 'exit'
while year != "exit":
  # Year should be input as a number
  year = input("Enter a year or type Exit: ")
  # Check if the year entered is actually a number
  if year.isnumeric():
    # Convert the string to an integer
    year = int(year)
    # Check if the year is odd
    if year % 2 != 0:
      print(year, "is a leap year.")
      print(year, "is odd.\n")
    # Check if the year is divisible by 10
    elif year % 10 == 0:
      print(year, "is a leap year.")
      print(year, "is divisible by 10.\n")
    # If the year is not odd or divisible by 10, it is not a leap year
    else:
      print(year, "is not a leap year.")
      print(year, "is not odd or divisible by 10.\n")
  else:
    # Quit program if the user has entered 'exit'
    if year.lower() == "exit":
      year = year.lower()
      print("Goodbye.\n")
    else:
      print("I don't understand. Try again.\n")
