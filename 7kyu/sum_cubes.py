"""
Sum of Cubes

Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

Assume that the input n will always be a positive integer.

Examples: (Input --> output)

2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)
"""
def sum_cubes(n):
    
    #declare output variable
    output = 0
    
    # iterate thru n+1
    for i in range(1,n+1,1):
        
        # raise i to third power and sum 
        output += i**3
    
    return output

#testing block
print ('actual result  :' + str(sum_cubes(1)) + '\n' +
       'expected result:' + '1' + '\n')

print ('actual result  :' + str(sum_cubes(2)) + '\n' +
       'expected result:' + '9' + '\n')

print ('actual result  :' + str(sum_cubes(123)) + '\n' +
       'expected result:' + '58155876' + '\n')