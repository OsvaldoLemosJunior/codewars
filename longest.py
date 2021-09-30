"""
Two to One

Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters 
- each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""
def longest(a1, a2):
    # your code
    
    #declare dictionary to store unique letters in both given strings
    arrOut = {}

    #return string with unique letters
    outputText = ''

    #iterates thru both strings
    for letter in a1 + a2:
        #store each letter in respective dictionary, already exiting letter will be overwritten
        arrOut[letter] = letter
    
    #sort dictionary keys and concatenate in a single string
    for key in sorted(arrOut.keys()):
        outputText = outputText + key
    
    return outputText

#testing block
print ('actual result  :' + longest('aretheyhere', 'yestheyarehere') + '\n' +
       'expected result:' + 'aehrsty' + '\n')

print ('actual result  :' + longest('loopingisfunbutdangerous', 'lessdangerousthancoding') + '\n' +
       'expected result:' + 'abcdefghilnoprstu' + '\n')

print ('actual result  :' + longest('inmanylanguages', 'theresapairoffunctions') + '\n' +
       'expected result:' + 'acefghilmnoprstuy' + '\n')