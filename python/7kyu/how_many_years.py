"""
Difference between years. (Level 1)

Write a function that receives two strings as parameter. This strings are in the following format of date: YYYY/MM/DD. Your job is: Take the years and calculate the difference between them.

Examples:
'1997/10/10' and '2015/10/10' -> 2015 - 1997 = returns 18 
'2015/10/10' and '1997/10/10' -> 2015 - 1997 = returns 18
At this level, you don't need validate months and days to calculate the difference.

"""
def how_many_years (date1,date2):

    #extract year only and store in specific variable    
    year1 = int(date1[:4])
    year2 = int(date2[:4])

    #if year1 is most recent than year2
    if (year1 - year2) > 0:
        return year1 - year2

    else:
        return year2 - year1


print(how_many_years('1997/10/10', '2015/10/10'))