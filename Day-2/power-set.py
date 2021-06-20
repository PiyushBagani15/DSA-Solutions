"""
Write a function that takes in an array of unique integers and returns its 
powerset. The powerset P(X) of a set X is the set of all subsets of X. For 
example, the powerset of [1,2] is [[], [1], [2], [1,2]].
Note that the sets in the powerset do not need to be in any particular 
order.
"""
def Powerset(set_inp):
    if set_inp == []: #base case
        return [[]]
    x = Powerset(set_inp[1:])
    #print(x)
    return ( x + [[set_inp[0]] + y for y in x])

# Driver Code
print(Powerset([1,2,3]))
