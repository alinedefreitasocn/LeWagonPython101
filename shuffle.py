""" Thanks to Python’s built in random library we have access to a shuffle method, 
which when called on a list - returns a shuffled version of that list. In this 
advanced exercise, let’s try to code a shuffle function ourselves from scratch.

Specs
Code a manual_shuffle function:

The function should take one argument, a list, and return a new list with all 
the items of your original list in a new, randomized order
Do Not use any built in list methods to manipulate the order such as sort()
Do Not use the built in shuffle method in python’s random library (let’s do it 
the hard way). But you might find some other helpful methods in there, we imported 
the random library for you at the top of the file 😉
Hint: You should not makes changes to the original List, the copy method will come 
in handy. One approach could be to create a new empty array B, and until A is empty, 
randomly select an index in A, append the element in A at that index into B, then delete 
that index in A. Proceed until A is empty. B should contain the new shuffled array! """
import random

def manual_shuffle(lis):
    lis_2 = lis.copy() 
    new_lis = []
    
    while len(lis_2) != 0:
        i = random.randrange(0, len(lis_2))
        new_lis.append(lis_2[i])
        del lis_2[i]
    return new_lis

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing your Shuffle's length:")
if len(manual_shuffle(list(range(20)))) == 20:
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's randomness:")
if manual_shuffle(list(range(100))) != manual_shuffle(list(range(100))):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your Shuffle's content vs. the original:")
if set(manual_shuffle(list(range(100)))) == set(range(100)):
	os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's destructiveness:")
test_list = list(range(10))
manual_shuffle(test_list)
if len(test_list) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your Shuffle's helper methods")
import dis
def list_method_calls(fn):
    methods = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for ix, instr in enumerate(instrs):
        if instr.opname=="CALL_METHOD":
            load_method_instr = instrs[ix + instr.arg + 1]
            methods.append(load_method_instr.argval)
    return methods

if "shuffle" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

if "sort" not in list_method_calls(manual_shuffle):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    




    
