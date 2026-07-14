import sys
import string


def text_analyzer(*r_string):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.

    Args:
        r_string (string): string to count the caracteres type.

    Returns:
        None
    """
    length = len(r_string)
    if length == 0 or r_string is None:
        print('What is the text to analyse?')
        o_string = input('>> ')
    else:
        o_string = r_string[0]
    try:
        if isinstance(o_string, str) is False:
            raise TypeError('AssertionError: argument is not a string')
        printable = 0
        nbUpper = 0
        nbLower = 0
        nbPoint = 0
        nbSpace = 0
        for c in o_string:
            if c.isprintable():
                printable += 1
                if c.islower():
                    nbLower += 1
                elif c.isupper():
                    nbUpper += 1
                elif c.isspace():
                    nbSpace += 1
                elif c in string.punctuation:
                    nbPoint += 1
        print(f"The text contains {printable} printable character(s):")
        print(f"- {nbUpper} upper letter(s)")
        print(f"- {nbLower} lower letter(s)")
        print(f"- {nbPoint} punctuation mark(s)")
        print(f"- {nbSpace} space(s)")
    except TypeError as e:
        print(f'{e}', file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('Usage: python3 count.py <string>')
        sys.exit()
    text_analyzer(sys.argv[1])
