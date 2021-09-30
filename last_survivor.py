def last_survivor(letters, coords): 
    # your code here
    
    for coord in coords:
        
        letters = letters[0:coord] + letters[coord+1:]
    
    return letters
