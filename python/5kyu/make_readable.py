"""
Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

""" 

def make_readable(seconds):
    #declare and initialize return variables
    hours = "00"
    minutes = "00"
    sec = "00"

    # modulus of division will be seconds
    sec = seconds % 60
    #print ('sec: ' + str(sec))
    # remove seconds from given number, as it was already calculated
    seconds -= sec

    if seconds < 3600:
        #print('tem minutos only')
        minutes = round(seconds / 60)
        print('minutes: ' + str(minutes))
    
    if seconds >= 3600:
        #print('tem minutos + horas')
     
        minutes = seconds % (3600)
        
        seconds -= minutes
        minutes = round(minutes/60)
        #print('minutes: ' + str(minutes))
        
        hours = round(seconds / (60*60))
        #print('hours: ' + str(hours))


    hours = hours.rjust(2,'0')
    minutes = str(minutes).rjust(2,'0')
    sec = str(sec).rjust(2,'0')

    ret = hours + ':' + minutes + ':' + sec

    return ret

make_readable(60)
