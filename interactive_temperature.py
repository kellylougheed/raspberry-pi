#!/usr/bin/env python
# Initialize response variable
response = ""
# Program should loop until the user inputs 'exit'
while response.lower() != "exit":
  # Temperature should be input as a number and a unit separated by a space
  # Split the input into a list consisting of the number and unit
  temp = input("Enter temperature in degrees F or C (e.g. 65 F or 18 C) or type 'Exit': ").split()
  # Check to see if there is a number and unit
  if len(temp) == 2:
    # Get the number an index 0 of the list
    num = temp[0]
    # Get the unit at index 1 of the list
    unit = temp[1]
    try:
      # Convert the number string to a float, if possible
      num = float(num)
      # Check if the unit is Fahrenheit
      if unit.upper() == "F":
        # Convert F to C
        print("Degrees in Celsius: ", (num - 32)/1.8, "\n")
      # Check if the unit is Celsius
      elif unit.upper() == "C":
        # Convert C to F
        print("Degrees in Fahrenheit: ", num * 1.8 + 32, "\n")
      else:
        print("I don't understand. Try again.\n")
    except:
      print("I don't understand. Try again.\n")
  elif len(temp) > 0 and temp[0].lower() == "exit":
    # Change the response variable to 'exit' and make the while loop stop
    print("Goodbye.\n")
    response = "exit"
  else:
    print("I don't understand. Try again.\n")
