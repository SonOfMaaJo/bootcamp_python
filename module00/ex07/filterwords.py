import sys
import string


def remove_punctuations(word: str) -> str:
    """function to remove punctuations from word"""
    new_word = ''
    for c in word:
        if c not in string.punctuation:
            new_word = new_word + c
    return new_word


def more_than_n_punct(word: str, number: int) -> bool:
    """function to check if word content more thant non punctuation number"""
    i: int = 0
    for c in word:
        if c not in string.punctuation:
            i += 1
    return i > number


if __name__ == '__main__':
    try:
        S = sys.argv[1]
        number = int(sys.argv[2])
        word_lists = S.split(' ')
        new_word_lists = [remove_punctuations(word) for word in word_lists
                          if more_than_n_punct(word, number)]
        print(new_word_lists)
    except (KeyError, ValueError, IndexError):
        print('ERROR')
