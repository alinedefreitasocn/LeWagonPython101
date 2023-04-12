
"""
Week zero on Le Wagon challenge
Function to return true if the number is colorful (where the products
of all the subsets of the digits are different.) given a tree digits number

It's working for two digits number as well, not sure why and if it was
supposed to be like this.

"""
def is_colorful(n):
    # iniciating an empty list
    li = []
    # it was suppose to count the number of digits
    i = 0
    # getting the separate digits of n
    while n > 0:
        li.append(n % 10)
        n = n // 10
        i =+ 1
    # multiplying digits
    li.append(li[0] * li[1])
    li.append(li[1] * li[2])
    li.append(li[0] * li[1] * li[2])

    # checking if all values are unique using set
    return len(set(li)) == len(li)
