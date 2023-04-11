''' Our function should take a single list of strings as an argument, containing our first opperand, 
followed by an operator and then the 2nd operand. eg:
simple_calculator(['1', '+', '1' ]) #=> 2
The function should return 'Please enter valid format: [Operand, Operator, Operand]' for arguments 
that don’t match the required format
The funtion should work with the following simple operators +, -, *, /, %, and should return'Please 
enter a valid operator [ +, -, /, *, % ]' if any other operators are passed
Assume that the operands are always numeric (floats or integers); no need to validate their data type '''
# Implement your simple_calculator function below

def simple_calculator(calc):
    if len(calc) == 3:
        if calc[1] == '+':
            return float(calc[0]) + float(calc[2])
        elif calc[1] == '-':
            return float(calc[0]) - float(calc[2])
        elif calc[1] == '*':
            return float(calc[0]) * float(calc[2])
        elif calc[1] == '/':
            return float(calc[0]) / float(calc[2])
        elif calc[1] == '%':
            return float(calc[0]) % float(calc[2])
        else:
            return 'Please enter a valid operator [ +, -, /, *, % ]'
    else:
        return 'Please enter valid format: [Operand, Operator, Operand]'
# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing your function's addition:")
if simple_calculator(['5', '+', '5']) == 10:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's subtraction:")
if simple_calculator(['10.5', '-', '5']) == 5.5:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's multiplication:")
if simple_calculator(['8', '*', '8']) == 64:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's division:")
if simple_calculator(['1', '/', '4']) == 0.25:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your function's modulo:")
if simple_calculator(['9', '%', '2']) == 1:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing your function's error handling:")
if simple_calculator(['1', '4']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '4', '5', '+']) == 'Please enter valid format: [Operand, Operator, Operand]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
if simple_calculator(['1', '&', '5']) == 'Please enter a valid operator [ +, -, /, *, % ]':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
