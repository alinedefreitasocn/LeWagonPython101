""" 
In this simple Kata your task is to create a function that turns a string into a 
Mexican Wave. You will be passed a string and you must return that string in an array 
where an uppercase letter is a person standing up. 

1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
 
 wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
 """

def wave(people):
    # Code here
    wav = []
    for i in range(len(people)):
        if people[i] == ' ':
            pass
        else:
            wav.append(people[:i].lower() + people[i].upper() + people[i+1:].lower())
    return wav
