import base64
import binascii
#XOR
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


# input string
input = '1c0111001f010100061a024b53535009181c'
XorString = '686974207468652062756c6c277320657965'
#convert to binary
binaryInput = binascii.unhexlify(input)
xorInput = binascii.unhexlify(XorString)

output = xor_strings(binaryInput, xorInput)
#convert binary to base 64
output = binascii.hexlify(output)

#print for niceness
print output