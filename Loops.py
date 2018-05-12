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
  
  
