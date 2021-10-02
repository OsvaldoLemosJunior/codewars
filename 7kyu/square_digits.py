"""
Square Every Digit

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""
    
def square_digits(num):
    
    #declare empty String to store output
    output = ''
    #iterate thru all chars in String
    for i in str(num):
        #convert to int apply power and convert back to string to concatenate
        output = output + str(int(i)**2)
    
    #convert to int before returning it
    return int(output)

print(str(square_digits(9119)))