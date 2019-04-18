# Build a list from 0 to 50 inclusively
my_list = range(51)

# List Comprehension - can generate lists using for/in and if 
# Build a list of even numbers from 0 to 50 inclusive

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# list for numbers 1 to 5
new_list= [x for x in range(1,6)]
# => [1,2,3,4,5]

# Doubled numbers
doubles = [x*2 for x in range(1,6)]
# => [2,4,6,8,10]

# Doubled numbers that are evenly divisible by 3
doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3==0]
# => [6]

# use a list comprehension to build a list even_squares that should contain the squares of even numbers between 1 to 11
# should start [4,16,36....] and so on

even_squares = [x**2 for x in range(1,12) if (x**2) %2 ==0]

print even_squares

c = ['C' for x in range(5) if x<3]
print c
# Use a list comprehension to create cubes_by_four 
# Should consist of the cubes of numbers 1 through 10 only if the cube is evenly divisible by 4

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four

# List Slicing 
# Only want part of a list > slicing allows access elements of a list in a concise manner
# Syntax: [start:end:stride]
# start > where to start, inclusive
# end > where to end, exclusive
# stride > space between items in the sliced list

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

# default start is 0, end is end of list, stride is 1 
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:] # starts at 3
# prints ['D', 'E'] 

print to_five[:2] # ends at 2
# prints ['A', 'B']

print to_five[::2] # stride is 2
# print ['A', 'C', 'E']

# Use slicing to print out every odd element of my_list from start to finish

my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]

# Positive stride > progresses through list from left to right
# Negative stride > right to left 

letters = ['A', 'B', 'C', 'D', 'E']
print letters [::-1]

# Reverse the list 
my_list = range(1, 11)

backwards = my_list[::-1]

# Print the result of going backwards by tens
to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# Create a list to_21 that the numbers 1 to 21 inclusive
to_21 = [i for i in range(1,22)]
# Create second list odds that contains only the odd numbers in to_21 using list slicing
odds = to_21[::2]
# Create a third list that's equal to the middle third of to_21 from 8 to 14 inclusive
middle_third = to_21[7:14:1]
