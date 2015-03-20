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
        if letter.isupper() and (random.randint(1,6) == 1): # 1 in 5 upper-case letters will be turned to lower-case
            out_text += letter.lower()
        else:
            out_text += letter
    return out_text

def get_nearby_char(char):

	if not char:
		return

	if not char in layout:
		return char

	for ix, row in enumerate(layout): # get index of char we want to manipulate
		for iy, i in enumerate(row):
			if i == char: # introduce the "typo", shift the index randomly by +-1
				while True:
					if i == ' ': # spacebar ...
						iy += random.randint(-1, +5) # ... is a bit bigger
					else:
						iy += random.randint(-1, +1)
					ix += random.randint(-1, +1)
					ix = max(min(len(layout)-1, ix), 0) # prevent out of bounds
					iy = max(min(len(layout[ix])-1, iy), 0)
					retval = layout[ix][iy]
					if retval != '': # make sure we return something even while processing a char surrounded by '' in the layout
						return retval

def wrong_key(text):

    # german keyboard layout
    global layout
    layout = ['^', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'ß', '`'], \
             [ '', 'q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü', '*'], \
             [ '', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', '#'], \
             [ '', '<', 'y', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',  ''], \
             [ '',  '',  '', '',  ' ', ' ', ' ', ' ', ' ',  '',  '',  '',  '']

    out_text = ''
    for letter in text:
        choice = random.randint(1,61)
        if choice <= 2:                     # 2 in 60 characters will be replaced with an adjacent letter (only lower-case)
            out_text += get_nearby_char(letter)
        elif choice == 4:                   # 1 in 60 characters will be followed by an adjacent letter
            out_text += letter + get_nearby_char(letter)
        elif choice == 7: # 1 in 60 characters will be skipped/deleted
            continue
        else:
            out_text += letter


    return out_text

def wrong_spelling(text):
    out_text = text
    common_mistakes = {' seid ':' seit ',
                        ' seit ':' seid ',
                        'wider':'wieder',
                        'wieder':'wider',
                        ', das':', dass',
                        ', dass':', das',
                        'standard':'standart',
                        'Standard':'Standart'}

    for written_word in common_mistakes.keys():
        out_text = out_text.replace(written_word, common_mistakes[written_word])

    return out_text

def double_capital(text):
	out_text, prev, old_letter = '', '', ''
	for letter in text:
		choice = random.randint(1,61)
		old_letter=letter
		if (choice <= 2) and (prev != '') and prev.isupper():
			letter = letter.upper()

		prev = old_letter
		out_text = out_text + letter

	return out_text


def obfucsate(text):
    # insert typos of all types
    text = wrong_spelling(text)
    text = miss_shift(text)
    text = wrong_key(text)
    text = double_capital(text)
    return text


test = "Kafka - Die Verwandlung.txt"
write_file(test, obfucsate(open_file(test)))
