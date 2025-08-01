def break_words(stuff):
    """This function splits the input string into words."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    word = break_words(sentence)
    return sort_words(word)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(s   entence):
    """Sorts the words the prints the first and last one."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
