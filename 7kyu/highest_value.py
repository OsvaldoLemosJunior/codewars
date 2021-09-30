def highest_value(a, b):
     
    countA = 0
    countB = 0
    
    for letter in a:
        countA += ord(letter)
    
    for letter in b:
        countB += ord(letter)
        
    if countA == countB:
        return a
    elif countA > countB:
        return a
    elif countA < countB:
        return b