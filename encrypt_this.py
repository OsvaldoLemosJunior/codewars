
"""
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
"""

def encrypt_this(text):
    
    #declare list to store encrypted words
    out = []
    #temporary variable for each encrypted word
    temp = ''
    
    #skip empty strings
    if text:
        #split string into words
        for word in text.split():
            
            #each string has at least one letter, apply rule for first letter
            temp = str(ord(word[0:1]))
            
            #if there is at least second letter, apply encryption rule for it
            if len(word) > 1:
                temp = temp + word[-1]
                
                #if there is at least one more letter, apply encryption rules for it
                if len(word) > 2:
                    temp = temp + word[2:len(word)-1] + word[1]

            #append temporary encrypted word in list of words            
            out.append(temp) 
    
    #join adding spaces between words and return full encrypted phrase
    
    return ' '.join(out)
     

#test block
print ('actual result  :' + encrypt_this('A wise old owl lived in an oak') + '\n' +
       'expected result:' + '65 119esi 111dl 111lw 108dvei 105n 97n 111ka' + '\n')

print ('actual result  :' + encrypt_this('The more he saw the less he spoke') + '\n' +
       'expected result:' + '84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp' + '\n')

print ('actual result  :' + encrypt_this('The less he spoke the more he heard') + '\n' +
       'expected result:' + '84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare' + '\n')

print ('actual result  :' + encrypt_this('Why can we not all be like that wise old bird') + '\n' +
       'expected result:' + '87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri' + '\n')

print ('actual result  :' + encrypt_this('Thank you Piotr for all your help') + '\n' +
       'expected result:' + '84kanh 121uo 80roti 102ro 97ll 121ruo 104ple' + '\n')

encrypt_this('') # 