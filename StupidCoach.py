""" In this exercise, we will create your own personal coach.
Unfortunately though, the coach is a little stupid and can only exhibit the following behavior:

If you don’t ask them something, but just tell them something (e.g. "I met a girl last night"), they will just
answer back "I don't care, get dressed and go to work!"
If you ask them something (e.g. "Can I eat some pizza?"), they won’t be of much help either and they will tell 
you "Silly question, get dressed and go to work!"
The only way to get rid of them is to tell them what they wants to hear: "I am going to work right now!".
Let’s make a comparison between the real world and the code world on this exercise.
The objectives of this challenge are:

Understand the flow of a program and learn how to “read” through your code, line by line
Learn about conditional statements
Learn about coding structures that modify your program flow
Specs

Coach answer
Define the coach_answer function line 2 in the code editor.

It should take one argument, your_message which is the sentence you tell the coach.
The function should return a str (i.e., the coach’s answer) which will obviously depend on which value is 
passed in your_message.
The function should not return anything if you tell the coach what they want to hear
Enhanced version
Now let’s implement an enhanced version. Define the function coach_answer_enhanced line 13. If you SHOUT at 
your coach, they will like it, and will say: I can feel your motivation! before the regular answer (from the 
non-enhanced version). Remember that shouting on the Internet is done by writing in CAPS LOCK! However, if you 
shout “I AM GOING TO WORK RIGHT NOW!”, your coach will leave you alone. """

# Implement your coach_answer method below:
def coach_answer(your_message):
    if your_message == "I am going to work right now!":
        return ''
    elif your_message[-1] == '?':
        return "Silly question, get dressed and go to work!"
    else:
        return "I don't care, get dressed and go to work!"

# Implement your coach_answer_enhanced below:
def coach_answer_enhanced(your_message):
    if your_message != your_message.upper():
        return coach_answer(your_message)
    else:
        if your_message == 'I AM GOING TO WORK RIGHT NOW!':
            return ''
        else:
            return 'I can feel your motivation! ' + coach_answer(your_message)


# Do not modify the code below:
print("##########################################")
print("###################TESTS###################")
print("##########################################\n")

import os
print("Testing coach_answer method")
print("------------------------------------------------------------------------\n")

print("Testing that coach_answer returns a str")
if type(coach_answer("Hello coach!")) == str:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer replies saying he does not care when you enter a statement")
if coach_answer("I would love to eat some pizza!")  == "I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer replies saying it\'s a silly question when you enter a question")
if coach_answer("Can I eat some pizza?") == "Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer does not answer back (i.e. answers with an empty string) when you tell him you are going to work")
if coach_answer( "I am going to work right now!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("\n")
print("Testing coach_answer_ennhanced method")
print("------------------------------------------------------------------------\n")

print("Testing that coach_answer_enhanced returns a str")
if type(coach_answer_enhanced("Hello coach!")) == str:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced replies saying he does not care when you enter a statement (and does not shout)")
if coach_answer_enhanced("I would love to eat some pizza!") == "I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced replies saying it\'s a silly question when you enter a question (and does not shout)")
if coach_answer_enhanced("Can I eat some pizza?") == "Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced does not answer back (i.e. answers with an empty string) when you tell him you are going to work (and does not shout)")
if coach_answer_enhanced( "I am going to work right now!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced prepends a motivation statement before saying he does not care when you shout a statement at him")
if coach_answer_enhanced("I WOULD LOVE SOME PIZZA!") == "I can feel your motivation! I don't care, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced prepends a motivation statement before saying that it\'s a silly question when you shout a question at him")
if coach_answer_enhanced("CAN I EAT SOME PIZZA?") == "I can feel your motivation! Silly question, get dressed and go to work!":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing that coach_answer_enhanced does not answer back (i.e. answers with an empty string) when you shout at him saying you are going to work")
if coach_answer_enhanced( "I AM GOING TO WORK RIGHT NOW!" ) == "":
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
