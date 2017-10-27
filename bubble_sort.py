#!/usr/bin/env python
# This program sorts a list of comma-separated integers using bubble sort

# Swaps two numbers in a list given their indices
def swap(l, index1, index2):
  temp = l[index2]
  l[index2] = l[index1]
  l[index1] = temp

numbers = input("Enter a list of comma-separated integers: ")
lst = numbers.split(",")
done = False
passes = 0
while not done:
  # Make done variable true so that it can be changed to false if the sorting is not yet done
  done = True
  for index, item in enumerate(lst):
    # If it's not the end of the list and the two adjacent items are out of order
    if index + 1 != len(lst) and lst[index] > lst[index + 1]:
      swap(lst, index, index + 1)
      # Make done variable false because the list was not done being sorted
      done = False
  passes += 1
  print("Pass %s: %s" %(passes, ",".join(lst)))
print("Original List: %s" %(numbers))
print("Sorted List: %s" %(",".join(lst)))
print("Passes: %s" %(passes))
