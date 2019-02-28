# Write a function that checks if number x is divisible by 2

def is_even(x):
  if x%2 == 0:
    return True
  else:
    return False

# ******* IS_INT ************
# Note: here a number with a decimal 0 is also an integer > ex. 7.0

# define a function is_int that takes a number x
def is_int(x):
  # return True if number is an integer and False otherwise
  # The difference between a number and that same number rounded is greater than zero
  if (x-round(x)) >= 0:
    return True
  else:
    return False
# ****** DIGIT_SUM *********
# Summing the digits of a number
# Takes positive int n and returns sum of all that number's digits
# Ex: 1234 should return 10 (assume always positive number)

def digit_sum(n):
  # convert n to string and iterate over and back into int
  sum = 0
  #strg = str(n)
  for i in str(n):
    sum += int(i)
  return sum

# ***** FACTORIAL *******
# Factorial of pos int x > multiply all ints from 1 to x
# Ex: factorial(4) = 4*3*2*1
def factorial(x):
  # calculate and return the factorial of number x 
  if x == 0:
    return 1
  else:
    return x*factorial(x-1)
  
print factorial(4)

# **** REVERSE TEXT ****

# Reverse takes string text and returns it in reverse
# Ex: abcd should return dcba
def reverse(text):
  l=len(text)
  t=''
  while (l > 0):
    # loop through text starting from the last character through the first
    l-=1
    t+=text[l]
  return t
   
print reverse("abcd")


# **** ANTI-VOWEL ******

# Define a function that takes a string input and returns it with all the vowels removed
def anti_vowel(text):
  new = ''
  for i in text:
    if i not in "aeiouAEIOU":
      new += i 
  return new

print anti_vowel("Hey You!")

# *** SCRABBLE SCORE ***

# # Define a function that takes a string word and returns the equivalent score for that word
# Dictionary with point values
# Assumptions: input 1 word with no spaces or punctuation
# > no score multipliers

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower() #make string lower case
  total = 0
  for i in word:
    total += score[i] #access value stored in dictionary
  return total

print scrabble_score("Helix")

# *** CENSOR ****

# Write a function censor that takes 2 strings and returns the string entered replaced with asterisks
# Assumptions: > input strings don't contain punctuation or upper case letters. 
# > Number of asterisks should correspond to the number of letters in the censored word

def censor(text, word):
  text = text.split()
  for i in range(len(text)):
    if text[i] == word:
      text[i]='*'*len(word)

  
  return " ".join(text)

print censor("this hack is wack hack", "hack")

