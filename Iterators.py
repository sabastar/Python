# Iterators for Dictonaries
# Create your own dictionary with 2-3 key/value pairs the print the result of calling .items()

my_dict = {
  "Name": "Sam",
  "Age": 44
}

print my_dict.items()
print my_dict.keys()
# .items() returns an array of tuples from the dictionary
# .keys() returns a list of dictionary's keys
# .values() returns a list of dictionary's values
# tuples are surrounded by () and can contain any data type

print my_dict.values()

# in operator
for number in range(5):
  print number, # comma to print each on same line

d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!

# For each key in dictionary, print out the key, space, value of that key

for key in my_dict:
  print key, my_dict[key]
  
  
  
