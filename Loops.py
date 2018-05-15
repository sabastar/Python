# Create a while loop that counts up to 9 (inclusive)
count = 0

if count <= 9:
  print "Hello, I am an if statement and count is", count

while count <= 9:
  print "Hello, I am a while and count is", count
  count += 1
  
  # Loop condition decides if loop will continue
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False

# Write a while loop that prints out all numbers from 0 to 10 squared inclusive
num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print num**2
  # Increment num (make sure to do this!)
  num += 1

choice = raw_input('Enjoying the course? (y/n)')

while choice!='y' and choice!='n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
  
# use break to exit a loop 
count = 0

while True:
  print count
  count += 1
  # use if statement to define the stopping condition
  if count >= 10:
    break # exit the loop

# While else > executes false condition
# it will execute if loop never entered or if loop exits normally, not after a break

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
  
  # Allow user to guess what number it is 3 times
  
  from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left > 0:
  # raw_input turns input into a string, wrap with int()
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  
  print "You lose."
  
# For loops > Make a for loop that counts from range 0 to 19
print "Counting..."

for i in range(20):
  print i
  
# Create a for loop that prompts user for a hobby 3 times and save result to hobby var
hobbies = []

# Add your code below!
for i in range(3):
  # save result of each prompt into hobby
  hobby = raw_input("Hobby: ")
  # append each one to hobbies
  hobbies.append(hobby)
  # print hobbies after the for loop
print hobbies


# Can print each individual character in a string using for loop 
# Add a second loop so that each character in word is printed one at a time

thing = "spam!"

for c in thing:
  print c

word = "eggs!"

# Your code here!
for x in word:
  print x
  
  
  
# Filter out the letter A in the string using a for loop
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print "X", 
# , prints on the same line
  else:
    print char,


#Don't delete this print statement!
print 

# loops with Lists:
numbers  = [7, 9, 12, 54, 99]
# num is next value in the list
print "This list contains: "

for num in numbers:
  print num

# Wrrite a second for loop that goes through numbers list and prints each element squared, each on its own line
for num in numbers:
  print num**2

 # Loop over a dictionary using the key to get the value
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Print the key with space and value associated
  print key + " " + d[key]
  
# ENUMERATION
choices = ['pizza', 'pasta', 'salad', 'nachos']

# enumerate supplies an index to each element in list that is passed > can count how many items
# index incremented, item is next item in sequence
# modify the print statement to start at index 1 
print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item
