"""
Return an output string that translates an input string s/$s by replacing each character in s/$s with a number representing the number of times that character occurs in s/$s and separating each number with the character(s) sep/$sep.

freq_seq("hello world", "-"); // => "1-1-3-3-2-1-1-2-1-3-1"
freq_seq("19999999", ":"); // => "1:7:7:7:7:7:7:7"
freq_seq("^^^**$", "x"); // => "3x3x3x2x2x1"
"""

def freq_seq(s, sep):

    #declare and initializa an array to store counts     
    arr = []
    #iterates thru all letters from string
    for letter in s:
        #add in array current count of occurences
        arr.append(str(s.count(letter)))

    #return joining with separator
    return (str(sep).join(arr))

freq_seq('hello world', '-') #'1-1-3-3-2-1-1-2-1-3-1'))
                             # 1-1-3-3-2-1-1-2-1-3-1-
                             # 1-1-3-3-2-1-1-2-1-3-1