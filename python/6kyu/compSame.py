"""
Are they the "same"?

Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, Elixir, Haskell, PureScript, Pascal, Perl, R, Rust, Shell).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
"""
def comp(array1, array2):
    
    print("array1: " + str(array1))
    print("array2: " + str(array2))
    
    if (array1) or (array1 is not None):
        
        # iterate thru array1
        for value in array1:
            
            #search each value power 2 in array2
            exists = value**2 in array2

            #if not found, return False
            if not exists:
                return False
            elif array1.count(value) != array2.count(value**2):
                return False

    else:
        return False
    
    if (array2) or (array2 is not None):        
    
        #iterate thru array2
        for value in array2:

            #search each value square root in array1
            exists = (value**0.5 in array1) or (-value**0,5 in array1)

            #if any value not found, return False
            if not exists:
                return False
    else:
        return False
    #any other case, return True
    return True

a1 = [2, 2, 3]
a2 = [4, 9, 9]
print(comp(a1, a2))