"""
Given a sentence, return it with all of the words longer than 5 characters
in a reverso mode
"""
def spin_it_or_not(word):
    if len(word) >= 5:
      print(f'The word {word} is too big! ')
      print(f'Reversing it: {word[slice(None, None, -1)]}')
      return word[slice(None, None, -1)]
    else:
      print(f'{word} a normal word')
      return word


def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    print(f'This is teh list of words: {words}')
    new_sentence = ''

    for word in words:
        if new_sentence != '':
            print(f'more than two words')
            print(f'{new_sentence}')
            new_sentence = new_sentence + ' ' + spin_it_or_not(word)
            print(f'{new_sentence}')
        else:
            print(f'This is the first word')
            print(f'{new_sentence}')
            new_sentence = new_sentence + spin_it_or_not(word)
            print(f'{new_sentence}')


    return new_sentence
