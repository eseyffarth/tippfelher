__author__ = 'Esther'
import random


def open_file(path):
    infile = open(path, "r", encoding="utf8")
    return infile.read()

def write_file(path, content):
    outpath = switch_letters(path.split('.',1)[0]) + '.' + path.split('.',1)[1]
    print(content, file=open(outpath, "w", encoding="utf8"))

def switch_letters(text):
    # swap two random adjacent letters
    if len(text) >1:
        first = random.randint(0,len(text)-2)       # first of switched letters may not be last letter of text
        second = first + 1
        out_text = text[0:first] + text[second] + text[first] + text[second+1:]

    return out_text

def miss_shift(text):
    out_text = ''
    for letter in text:
        if letter.isupper():
            choice = random.randint(1,6)            # 1 in 5 upper-case letters will be turned to lower-case
            if choice == 1:
                out_text += letter.lower()
            else:
                out_text += letter
        else:
            out_text += letter
    return out_text


def wrong_key(text):
    adjacent_keys = {'1':set(['2','q']),
                    '2':set(['1','q','w','3']),
                    '3':set(['2','w','e','4']),
                    '4':set(['3','e','r','5']),
                    '5':set(['4','r','t','6']),
                    '6':set(['5','t','z','7']),
                    '7':set(['6','z','u','8']),
                    '8':set(['7','u','i','9']),
                    '9':set(['8','i','o','0']),
                    '0':set(['9','o','p','ß']),
                    'ß':set(['0','ü']),
                    'q':set(['1','2','w','a']),
                    'w':set(['q','2','3','e','s','a']),
                    'e':set(['w','3','4','r','d','s']),
                    'r':set(['e','4','5','t','f','d']),
                    't':set(['r','5','6','z','g','f']),
                    'z':set(['t','6','7','u','h','g']),
                    'u':set(['z','7','8','i','j','h']),
                    'i':set(['u','8','9','o','k','j']),
                    'o':set(['i','9','0','p','l','k']),
                    'p':set(['o','0','ß','ü','ö','l']),
                    'ü':set(['p','ß','+','ä','ö']),
                    'a':set(['q','w','s','y','<']),
                    's':set(['a','w','e','d','x','y']),
                    'd':set(['s','e','r','f','c','x']),
                    'f':set(['d','r','t','g','v','c']),
                    'g':set(['f','t','z','h','b','v']),
                    'h':set(['g','z','u','j','n',]),
                    'j':set(['h','u','i','k','m','n']),
                    'k':set(['j','i','o','l',',','m']),
                    'l':set(['k','o','p','ö','.',',']),
                    'ö':set(['l','p','ü','ä','-','.']),
                    'ä':set(['ö','ü','+','#','-']),
                    'y':set(['<','a','s','x']),
                    'x':set(['y','s','d','c',' ']),
                    'c':set(['x','d','f','v',' ']),
                    'v':set(['c','f','g','b',' ']),
                    'b':set(['v','g','h','n',' ']),
                    'n':set(['b','h','j','m',' ']),
                    'm':set(['n','j','k',',',' ']),
                    ',':set(['m','k','l','.',' ']),
                    '.':set([',','l','ö','-']),
                    '-':set(['.','ö','ä']),
                    ' ':set(['x','c','v','b','n','m',','])}
    out_text = ''
    for letter in text:
        choice = random.randint(1,61)
        if choice <= 2:                     # 2 in 60 characters will be replaced with an adjacent key (only lower-case)
            if letter in adjacent_keys:
                out_text += random.sample(adjacent_keys[letter],1)[0]
            else:
                out_text += letter
        elif choice == 4:                   # 1 in 60 characters will be followed by an adjacent letter
            if letter in adjacent_keys:
                out_text += letter + random.sample(adjacent_keys[letter],1)[0]
        else:
            out_text += letter


    return out_text


def obfucsate(text):
    # insert typos of all types
    text = miss_shift(text)
    text = wrong_key(text)
    return text


test = "Kafka - Die Verwandlung.txt"
write_file(test, obfucsate(open_file(test)))