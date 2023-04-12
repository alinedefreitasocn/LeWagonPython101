"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

# terrible solution. I would like to make a better one next time.
# it was an exercise about dictionaries so we should use it.
# there is a great better solution not using dictionaries:
# def duplicate_count(s):
#  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    count = 0
    # first: separate the string into letters
    # creating a dictionary with every letter as a key
    repetition = {letter:0 for letter in text}

    # counting the letters
    for letter in text:
        repetition[letter] +=1

    for times in repetition.values():
        if times > 1:
            count += 1

    return count

    # third print how many letters repeat

    # challenge: do this using dictionaries

# Second try: much better using the solution I saw but still a dictionary

def duplicate_count(text):
    # Your code goes here
    text = text.lower()


    # first: separate the string into letters
    # creating a dictionary with every letter as a key
    repetition = {letter: text.count(letter) for letter in text if text.count(letter) > 1}

    # counting the letters
    # for letter in text:
    #    repetition[letter] +=1

    # for times in repetition.values():
    #    if times > 1:
    #        count += 1

    return len(repetition)
