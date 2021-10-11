"""
ASCII Fun #1: X- Shape

You will get an odd integer n (>= 3) and your task is to draw an X. Each line is separated with \n.

Use the following characters: ■ □ 

Examples

                                     ■□□□■
            ■□■                      □■□■□
  x(3) =>   □■□             x(5) =>  □□■□□
            ■□■                      □■□■□
                                     ■□□□■

"""
# -*- coding: utf-8 -*-
def x(n):
    
    #declare 2 dictionaries(1st for each line, and 2nd to store all lines)
    line = []
    dict = []
    
    #iterates thru n+1
    for i in range(1, n+1, 1):
        #declare line filled with 0
        line = ["□"]*n
        
        #if middle of line(only one '1' should be add in middle of line)
        if i == (n+1)/2:
            line[i-1] = '■'
        
        #all other cases
        else:
            #from right to letter find position of '1'
            line[i-1] = '■'
            #reverse, for left to right
            line[n-i] = '■'
            
        dict.append(''.join(line))
    return '\n'.join(dict)
    
    


#testing block
x(11)
