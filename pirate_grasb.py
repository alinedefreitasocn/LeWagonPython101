"""
Write a function that will accept a jumble of letters as well as a
dictionary, and output a list of words that the pirate might have meant.

ex.
grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
Should return ["sport", "ports"].
Return matches in the same order as in the dictionary.
Return an empty array if there are no matches.
"""
# It was supposed to be solved using dictionaries
def grabscrab(said, possible_words):
    right_words = []
    l_said = {letters: said.lower().count(letters) for letters in set(said)}
    for w in possible_words:
        l_possible = {letters: w.lower().count(letters) for letters in set(w)}

        if all(l_possible.get(key) == l_said.get(key) for key in l_possible):
            if all(l_said.get(key) == l_possible.get(key) for key in l_said):
                right_words.append(w)

    return right_words

"""
Outra solucao interessante que nao usa dicionario, usa o metodo de ordenamento
direto na string!

def grabscrab(said, possible_words):
    return [ word for word in possible_words if sorted(word) == sorted(said) ]
"""
