"""
You're given two positive integers representing the height of a staircase and 
the maximum number of steps that you can advance up the staircase at a 
time. Write a function that returns the number of ways in which you can 
climb the staircase.
For example, if you were given a staircase of height = 3 and maxSteps = 2 you 
could climb the staircase in 3 ways. You could take 1 step, 1 step, then 1 step,
you could also take 1 step, then 2 steps , and you could take 1 step, then 2 
steps , and you could take 2 steps, then 1 step.

"""

def staircase_traversal(height,max):
    # Recursive function used by countWays
  if height <= 1:
      return height
  res = 0
  i = 1
  while i<=max and i<=height:
      res = res + staircase_traversal(height-i, m)
      i = i + 1
  return res

# Returns number of ways to reach s'th stair    
def countWays(s,m):
  return staircase_traversal(s+1, m)
# Driver program

s,m = 4,2
print("Number of ways =",countWays(s, m))