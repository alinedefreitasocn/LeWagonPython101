""" We can break a number into different contiguous sub-subsequence parts. For example, the number 324 
can be broken into parts like (3, 2, 4, 32, 24, 324). A colorful number is a number where the products 
of all the subsets of the digits are different. eg:

263 is a colorful number (2, 6, 3, 2x6, 6x3, 2x6x3) are all different
236 is not (2, 3, 6, 2x3, 3x6, 2x3x6) has 6 twice (6 and 2x3)

Specs
We want you to write a function is_colorful which takes a single number as an argument and returns True 
if the number is colorful, False otherwise.

For this exercise, only consider numbers with up to 3 digits (not more), eg:
is_colorful(263) #=> True
is_colorful(236) #=> False"""

# Implement your is_colorful method below
def is_colorful(n):
    # iniciating an empty list
    li = []
    # i = 0
    # getting the separate values of n
    while n > 0:
        li.append(n % 10)
        n = n // 10
        # i =+ 1
    # multiplying values
    li.append(li[0] * li[1])
    li.append(li[1] * li[2])
    li.append(li[0] * li[1] * li[2])
    
    return len(set(li)) == len(li)
