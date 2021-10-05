"""
Buddy Pairs

You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil or (for Dart) null; (for Lua, Pascal, Perl) [-1, -1].

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
"""
def buddy(start, limit):

    #formulas:
    # s(m) = n + 1
    # s(n) = m + 1

    #declare variable to store sums
    sumN = 0
    sumM = 0
    
    for n in range(start, limit+1, 1):

        # reset vars.
        sumN = 0
        sumM = 0
        # list that will store divisors
        divs = [1]

        # loop thru range, square root because numbers must be primes
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                # add i to list of divisor and n/i
                divs.extend([i,int(n/i)])
        
        # sum all UNIQUE values from divisor
        sumN = sum(list(dict.fromkeys(divs)))

        # calculate m
        m = sumN - 1

        # search only for values for m > n
        if (m > n):
            
            #reset list
            divs = [1]

            # loop thru range for getting sum(m)
            for j in range(2, int(m**0.5) + 1):
                if m % j == 0:
                    # add divsor
                    divs.extend([j,int(m/j)])

            # sum all UNIQUE divisor
            sumM = sum(list(dict.fromkeys(divs)))
            
            # check condition on task:
            if (sumN == m + 1) and (sumM == n + 1):
                
                # return pair if condition is matched
                return [n,m]
    
    # in case on any pair found, return string
    return 'Nothing'

print(buddy(310, 2755)) # [1050, 1925]