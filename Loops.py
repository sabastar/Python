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

