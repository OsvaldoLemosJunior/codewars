"""
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""
def digital_root(n):

    # cast n into String
    n = str(n)
    # create counter var
    c = 0
    
    # keep sum till unique number
    while len(n) != 1:
        # iterates thru all chars
        for i in n:
            #sum
            c += int(i)

        #when level is done, replace n = counter and make counter 0    
        n = str(c)
        c = 0

    # return converting to int    
    return int(n) 

digital_root(942)