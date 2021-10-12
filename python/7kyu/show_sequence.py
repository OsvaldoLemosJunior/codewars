"""
Sum of numbers from 0 to N

Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

> 6
Output:

0+1+2+3+4+5+6 = 21

Input:

> -15
Output:

-15<0

Input:

> 0
Output:

0=0
"""

def show_sequence(n):

    # declare dictionary to separete string from integers
    arr = {}
    
    # check if number is positive
    if n > 0:
        #go thru till n+1 (n must be included)
        for i in range(0,n+1,1):
            # add key as string and value as integer
            arr[str(i)] = i

        # built output string    
        return ('+'.join(arr.keys()) + ' = ' + str(sum(arr.values())))

    # special treatment
    elif n == 0:
        return ('0=0')
    else:
        return (str(n)+"<0")

show_sequence(6)