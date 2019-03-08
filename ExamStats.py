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

# Use grades_sum to calculate the AVERAGE test grade

def grades_average(grades_input):
  gsum=grades_sum(grades_input)
  
  return grades_sum(grades_input)/float(len(grades_input))

print grades_average(grades)

# Variance - how grades varied against the average (smaller = closer to average)
def grades_variance(scores):
  average= grades_average(scores)
  variance=0 # rolling sum
  
  for score in scores: #compute its squared difference
    variance+= (average-score)**2
  return variance/len(scores)

print grades_variance(grades)

# Standard Deviation - square root of the variance, can calculate square root by raising the number to the one-half power

def grades_std_deviation(variance):
  return variance **0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)
