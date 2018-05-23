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
