"""
Which string is worth more?

You will be given two ASCII strings, a and b. Your task is write a function to determine which one of these strings is "worth" more, and return it.

A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string HELLO has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.

In the event of a tie, you should return the first string, i.e. a.
"""
def highest_value(a, b):

    #define counters 
    countA = 0
    countB = 0
    
    #calculate sum of ascii values for all letters in first word
    for letter in a:
        countA += ord(letter)
    
    #calculate sum of ascii values for all letters in second word
    for letter in b:
        countB += ord(letter)

    #if counters are same, return first. Otherwise return first or second.  
    if countA == countB:
        return a
    elif countA > countB:
        return a
    elif countA < countB:
        return b

print ('actual result  :' + highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567") + '\n' +
       'expected result:' + 'KkLlMmNnOoPp4567' + '\n')