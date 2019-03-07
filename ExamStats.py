# MINI PROJECT: Create a program to compute stats

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# Write a function to print out the list of grades, one element at a time
def print_grades(grades_input):
  
  #iterate through list and print each item on its own line
  for i in grades_input:
    print i
    
print_grades(grades)

# Create another function to compute the sum of all the test grades - without using SUM function

def grades_sum(grades):
  total = 0
  for i in grades:
    total+= i
  return total

print grades_sum(grades)

# 
