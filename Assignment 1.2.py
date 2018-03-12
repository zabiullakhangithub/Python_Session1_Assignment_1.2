# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:06:03 2018

@author: zabiulla.khan
"""

"""
Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

# Create a list with a range between 2000 and 3200
list1 = list(range(2000,3200))

# initialize the iterator to 0
i=0

'''create a new empty list to store all the numbers within range that 
are divisble by 7 and not multiples of 5'''
list2 = []

# Loop all the items in initial defined list range
for i in list1:
    
    #identify all the numbers divisible by 7 within range defined above
    div7 = i%7
    
    # identify all numbers which are multiples of 5 within the range defined above
    mul5 = i%5
    
    # Check if numbers are divisble by 7 and are not multiples of 5
    if div7 == 0 and mul5 != 0:
        # store/append all the numbers identified divisble by 7 and not multiples of 5
        list2.append(str(i))
#Include a comma seperator        
print(','.join(list2))

    
