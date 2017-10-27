#!/usr/bin/env python
# This program translates a string to Pig Latin

sentence = input("Type in a sentence to translate to Pig Latin: ")
vowels = ['a', 'e', 'i', 'o', 'u']
# Split sentence into a list of words
words = sentence.split()
for i, word in enumerate(words):
  # Split each word into a list of letters
  letters = list(word)
  first_vowel = 0
  # Loop through letters of the word to find the first vowel
  for j, letter in enumerate(letters):
    if letter.lower() in vowels:
      first_vowel = j
      break
  # Add 'yay' if the word starts with a vowel
  if first_vowel == 0:
    word = word + "yay"
  # Otherwise, move the beginning consonants + 'ay' to the end of the word
  else:
    word = word[first_vowel:len(word)] + word[0:first_vowel] + "ay"
  # Replace the English word with the Pig Latin word in the list
  words[i] = word.lower()
# Reconstructs a new Pig Latin sentence from the list of words
sentence = " ".join(words)
print(sentence)
