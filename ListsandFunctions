n = [1, 3, 5]

# Add your code below to print out the second element in the list

print n[1]

# Multiply the 2nd element of n by 5 and overwrite the 2nd element with that result
# print the list 
n[1] = n[1]*5
print n

# Append the number 4 to the end of the list n
n.append(4)
print n

n = [1, 3, 5]
# Remove the first item in the list here
#n.pop(index) remotes item at index from the list and return it to you
n.pop(0)

print n

# n.remote(item) will remote item IF it finds it (NOT an index but the actual item)
n.remove(1)
print n

# del(n[1]) is like .pop, it will remove the item at index but wont return it 
del(n[1]) # doesn't return anything
print n

m = 5
n = 13
# Add add_function here that has 2 parameters and adds them together
def add_function(x,y):
  return x+y


print add_function(m, n)


# write a function that takes a string and returns concatenated with world
n = "Hello"
def string_function(s):
  return s + 'world'


print string_function(n)

# Can pass a list as an argument
# Return the item stored in index 1 of x

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

# Change it to add 3 to item at index 1 of the list
def list_function(x):
  x[0] = x[0]+3
# Store the result back into index 1 
# return the list
  return x

n = [3, 5, 7]
print list_function(n)

# Function that appends number 9 to lst and return the modified list
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
 return lst.append(9)

print list_extender(n)

# Print each element one by one then call the function with argument n 
n = [3, 5, 7]

def print_list(x):
  for i in range(0,len(x)):
    print x[i]

print_list(n)

#Create function that takes a list and multiplies each element by 2 and returns that list
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i]*2
    print x[i]
# Don't forget to return your new list!

double_list(n)

# range() is a shortcut for generating a list
# Returns a list of numbers from start up to and (not including) stop. Each increases by a step
# 3 diff types > range(stop), range(start,stop), range(start, stop, step)
#start default 0 and step default 1 

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

#return a list that contains [0,1,2]
print my_function(range(0,3,1)) # Add your range between the parentheses!

#iterating through a list using range
# Method 1 > loop but not modify
# for item in list:
#  print item

# Method 2 > index to loop and can modify
# for i in range(len(list)):
#    print list[i]

# create a function that returns sum of a list of numbers
n = [3, 5, 7]

def total(numbers):
  result = 0 
  # iterate through numbers list and for each number add it to result
  for item in range(len(numbers)):
    result = result + numbers[item]
  # return result
  return result

print total(n)

# Create a function that concatenates strings

n = ["Michael", "Lieberman"]
# Define function that takes a list
def join_strings(words):
  # set result to empty string
  result = ""
  # iterate through words list and append each word to result
  for i in range(len(words)):
   result += words[i]
  return result


print join_strings(n)

# Create a function that joins two lists together
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x+y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

# Flatten function that takes a single list and concatenates all sublists that are part of it into a single list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  # Make a new empty list
  results = []
  for numbers in lists:
    # iterate through numbers
    for item in numbers:
      results.append(item)
  
  return results

print flatten(n)
