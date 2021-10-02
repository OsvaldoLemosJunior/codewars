"""
Kingdoms Ep1: Jousting

The King organizes the jousting. You are a young human lady and your fiancé is an ogre. Today is his anniversary and he would love to visit the tournament, but it's forbidden for ogres to visit the Kingdom. So you decided to go there, to paint the exact moments of clash of cavalry and to present these paintings to your beloved.

You are given the array / tuple (listField) of two strings of equal length. Each the string contains "$->" and "<-P"(knight with spear) respectively. The knights move towards each other and they can only take simultaneous steps of length vKnightLeft and vKnightRight. When the index of ">" is equal or more than the index of "<", return the array / tuple representing the knights' positions.

Some examples of the collision:

  ["$->  ",  
   "  <-P"]     
  ["   $-> ",
   "    <-P"]
  ["   $-> ",
   "   <-P "]
Notes:
"The knight "$->" always starts in the position 0 of the first string;
"The knight "<-P" always starts in the last position of the second string;
Velocity of knights can be different from 0 to 3 inclusive;
Sometimes the collision can happen immediately;
Sometimes there is no an immediate collision and velocitity of both knights is 0. At this case return an original array / tuple.
Example 1:

given
listField = ["$->    ",
             "    <-P"]
             
vKnightLeft = 1
vKnightRight = 1  

return
 [" $->   ", 
  "   <-P "]
Example 2:

given
listField = ["$->",
             "<-P"]
             
vKnightLeft = 1
vKnightRight = 1  

return
 ["$->", 
  "<-P"]
"""

def joust(list_field: tuple, v_knight_left: int, v_knight_right: int) -> tuple:
    
    kleft = list_field[0]
    kright = list_field[1]
    
    print (kleft)
    print (kright)
    
    for i in range(1, len(kleft),1):
        if (kleft.index('>') < kright.index('<') or 
            (kleft.index('>') < kright.index('-'))):
            
            kleft = ' '*v_knight_left + kleft[0:len(kleft)-v_knight_left]
            kright = kright[v_knight_right:] + ' '*v_knight_right
        
            print (kleft)
            print (kright)

    return (kleft, kright)

print(joust(("$->                                       ", "                                       <-P"), 0, 4))