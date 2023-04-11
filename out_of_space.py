""" Kevin is noticing his space run out! Write a function that removes the spaces from the values 
and returns an array showing the space decreasing. For example, running this function on the array 
['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']."""

def spacey(array):
    no_space = [array[0]]
    for i in range(len(array)-1):
        no_space.append(no_space[i] + array[i+1])
        
    return no_space
