import sys

morse_code_dict: dict[str, str] = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

if len(sys.argv) == 1:
    print('Usage: python3 sos.py [STRING ...]')
    sys.exit()
try:
    word = '  '.join(sys.argv[1::1])
    trans_word = ''
    i = 0
    for c in word:
        if c == ' ':
            trans_word = trans_word + '/ '
            i += 1
            continue
        trans_word = trans_word + morse_code_dict[c.upper()]
        i += 1
        if i != len(word):
            trans_word += ' '
    print(trans_word)
except KeyError:
    print('ERROR')
