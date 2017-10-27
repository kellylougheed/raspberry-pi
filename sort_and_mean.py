#!/usr/bin/env python

numbers = [3,9,7,4,0,2]

# Function that sorts a list of numbers, prints the sorted list, and returns the mean
def sort_and_mean(lst):
  total = 0
  done = False
  while not done:
    # Make done variable true so that it can be changed to false if the sorting is not yet done
    done = True
    for index, item in enumerate(lst):
      # Keep looping if it's the last item of the list OR if the items are already sorted
      if index + 1 == len(lst) or lst[index] < lst[index + 1]:
        continue
      # Otherwise, switch items to sort them
      elif lst[index] > lst[index + 1]:
        temp = lst[index + 1]
        lst[index + 1] = lst[index]
        lst[index] = temp
        # Make done variable false because the list was not done being sorted
        done = False
      total += lst[index]
  print(lst)
  return total/len(lst)
  
print(sort_and_mean(numbers))
