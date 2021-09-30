def swap_vowel_case(st): 
    # your code here
    
    dict = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U', 
            'A':'a', 'E':'e', 'I':'i', 'O':'o', 'U':'u'}
    
    msg = ''
    for letter in st:
        if letter in dict:
            msg += dict[letter]
        else:
            msg += letter
    
    return msg