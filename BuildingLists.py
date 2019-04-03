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
