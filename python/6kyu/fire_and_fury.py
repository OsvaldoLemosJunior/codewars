"""
FIRE and FURY

The President's phone is broken
He is not very happy.

The only letters still working are uppercase E, F, I, R, U, Y.

An angry tweet is sent to the department responsible for presidential phone maintenance.

Kata Task
Decipher the tweet by looking for words with known meanings.

FIRE = "You are fired!"
FURY = "I am furious."
If no known words are found, or unexpected letters are encountered, then it must be a "Fake tweet."

Notes
The tweet reads left-to-right.
Any letters not spelling words FIRE or FURY are just ignored
If multiple of the same words are found in a row then plural rules apply -
FIRE x 1 = "You are fired!"
FIRE x 2 = "You and you are fired!"
FIRE x 3 = "You and you and you are fired!"
etc...
FURY x 1 = "I am furious."
FURY x 2 = "I am really furious."
FURY x 3 = "I am really really furious."
etc...
Examples
ex1. FURYYYFIREYYFIRE = "I am furious. You and you are fired!"
ex2. FIREYYFURYYFURYYFURRYFIRE = "You are fired! I am really furious. You are fired!"
ex3. FYRYFIRUFIRUFURE = "Fake tweet."
"""

def fire_and_fury(tweet):

    print(tweet)
    fireArr = []
    furyArr = []
    fArr = []
    fireCounter = 0
    furyCounter = 0
    wordCounter = 0
    msg = ''
    ret = ''

    for i in range(0, len(tweet), 1):
        
        if tweet[i:i+4] == 'FIRE':
            #print (tweet[i:i+4])
            fireArr.append(wordCounter)
            wordCounter += 1
            fArr.append('FIRE')
            msg += 'FIRE'

        if tweet[i:i+4] == 'FURY':
            #print (tweet[i:i+4])
            furyArr.append(wordCounter)
            wordCounter += 1
            fArr.append('FURY')
            msg += 'FURY'

    for i in range(0,len(msg), 4):
        print ('abc: ' + msg[i:i+4])

        if (msg[i:i+4] == 'FURY'):
            if (msg[i+4:i+4+4] == 'FURY'):
                if (msg[i+4+4:i+4+4+4] == 'FURY'):
                    ret += "I am really really furious."
                    i += 8
                else:
                    ret += "I am really furious."
                    i += 4
            else:
                ret += "I am furious."
        else:
            if (msg[i:i+4] == 'FIRE'):
                if (msg[i+4:i+4+4] == 'FIRE'):
                    if (msg[i+4+4:i+4+4+4] == 'FIRE'):
                        ret += "You and you and you are fired!"
                        i += 8
                    else:
                        ret += "You and you are fired!"
                        i += 4
                else:
                    ret += "You are fired!"

        
    print ('ret: ' + ret)





    print ("fireArr: " + str(fireArr))
    print ("furyArr: " + str(furyArr))

fire_and_fury("FURYYYFIREYYFIRE")
