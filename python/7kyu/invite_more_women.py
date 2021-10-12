"""
Simple Fun #152: Invite More Women?

"""

def invite_more_women(arr):
    
    countMan = 0
    countWoman = 0

    for a in arr:
        if a == -1:
            countWoman += 1
        else:
            countMan += 1

    if countWoman >= countMan:
        return False
    else:
        return True



invite_more_women([1, -1, 1]) # True