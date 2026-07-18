from typing import Generator
from random import choice


def generator(text, sep=" ", option=None) -> Generator:
    '''
    Splits the text according to sep value and yields the substring
    '''
    if not isinstance(text, str):
        iterator = ["ERROR"]
    else:
        iterator = text.split(sep)
        iterator = [word for word in iterator if word != '']
        list_words = []
        if option == 'unique':
            for word in iterator:
                if word not in list_words:
                    list_words.append(word)
            iterator = list_words
        elif option == 'ordered':
            iterator = sorted(iterator)
        elif option == 'shuffle':
            lenght = len(iterator)
            for i in range(lenght):
                word = choice(iterator)
                list_words.append(word)
                iterator.remove(word)
            iterator = list_words
        else:
            iterator = ["ERROR"]
    for word in iterator:
        yield word
