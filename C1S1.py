import base64
import binascii
# input string
input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

#convert to binary
binary = binascii.unhexlify(input)

#convert binary to base 64
output = base64.b64encode(binary)

#print for niceness
print output