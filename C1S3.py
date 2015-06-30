import base64
import binascii
import collections
from collections import Counter


ENGLISH_FREQUENCIES = {
    'E': .1202,
    'T': .0910,
    'A': .0812,
    'O': .0768,
    'I': .0731,
    'N': .0695,
    'S': .0628,
    'R': .0602,
    'H': .0592,
    'D': .0432,
    'L': .0398,
    'U': .0288,
    'C': .0271,
    'M': .0261,
    'F': .0230,
    'Y': .0211,
    'W': .0209,
    'G': .0203,
    'P': .0182,
    'B': .0149,
    'V': .0111,
    'K': .0069,
    'X': .0017,
    'Q': .0011,
    'J': .0010,
    'Z': .0007,
}


#XOR
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def single_xor(binarystring, xor_char):
	return xor_strings(binarystring, chr(xor_char)*len(binarystring))

## Plagarized functions
def partition(pred, iterable):
    "Return a pair of lists; elements that satisfy pred, and those that don't."
    # No cuteness because I only want to inspect each element once.
    sat = []
    unsat = []
    for e in iterable:
        if pred(e):
            sat.append(e)
        else:
            unsat.append(e)
    return sat, unsat


#looks for english like language
def english_probability(text):
    """
    Returns a float representing the likelihood that the given text is a
    plaintext written in English. Range: (0.0 - 1.0), higher is better.
    """
    # Ignore whitespace (revisit this later).
    text = text.upper()
    letters, other = partition(lambda c: c in ENGLISH_FREQUENCIES, text)
    if not letters: return 0.0
    # Expect roughly 15% of text to be spaces.
    spaces, other = partition(lambda c: c.isspace(), other)
    space_error = abs(float(len(spaces))/len(text) - 0.15)
    # As a rough approximation, expect 2% of characters to be punctuation.
    punc_error = abs(float(len(other))/len(text) - 0.02)
    counts = Counter(text)
    letter_error = 0.0
    for c, target_freq in ENGLISH_FREQUENCIES.items():
        letter_error += (target_freq *
                        abs(float(counts.get(c, 0))/len(letters) - target_freq))
    return max(1.0 - (punc_error + letter_error + space_error), 0.0)


##end plagarized functions

# input string
input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#convert to binary
binaryInput = binascii.unhexlify(input)

decodeChar = 0
detectScore = 0.0
for i in range(1,255):
	output = single_xor(binaryInput, i)
	blah = english_probability(output)
	if detectScore < blah:
		detectScore = blah
		decodeChar = i

print single_xor(binaryInput, decodeChar)
print "Char was: ", chr(decodeChar)

#Character is 120

