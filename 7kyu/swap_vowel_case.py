"""
Strings: swap vowels' case

Challenge:

Given a string, return a copy of the string with the vowels' case swapped.

For this kata, assume that vowels are in the set "aeouiAEOUI".

Example: Given a string "C is alive!", your function should return "C Is AlIvE!"

Addendum: Your solution is only required to work for the ASCII character set.

Please make sure you only swap cases for the vowels.
"""
def swap_vowel_case(st): 
    # your code here
    
    #define dictionary with replacement rule
    dict = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U', 
            'A':'a', 'E':'e', 'I':'i', 'O':'o', 'U':'u'}
    
    #define return message variable
    msg = ''

    #iterate thru given string
    for letter in st:

        #check if letter exists in dictionary
        if letter in dict:
            #add replaced letter
            msg += dict[letter]
        else:
            #just add letter without changing
            msg += letter
    
    return msg

print ('actual result  :' + swap_vowel_case(" ") + '\n' +
       'expected result:' + " " + '\n')

print ('actual result  :' + swap_vowel_case("C Is AlIvE!") + '\n' +
       'expected result:' + "C is alive!" + '\n')

print ('actual result  :' + swap_vowel_case("to") + '\n' +
       'expected result:' + "tO" + '\n')

print ('actual result  :' + swap_vowel_case("The") + '\n' +
       'expected result:' + "ThE" + '\n')