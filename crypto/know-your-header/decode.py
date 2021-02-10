#!/usr/bin/env python2
import sys

def decode(data, key):
    
    # Initialize the return value of the function to an empty string
    res = ""

    # Iterate over all the bytes in data
    for i in xrange(0, len(data)):
        k = key[i % len(key)] 
        encoded_val = data[i]
        ord_c_xor_ord_k = ord(encoded_val)
        ord_c = ord_c_xor_ord_k ^ ord(k)
        c = chr(ord_c)
        res += c
    return res

if __name__ == "__main__":
    
    # Verifiy the arguments passed to the script 
    # are ok.
    if len(sys.argv) < 4:
        print "Usage: {} key_hex input output".format(sys.argv[0])
        sys.exit(-1)
    if (len(sys.argv[1]) % 2 == 1):
        print "Invalid key length. It needs to be an even number."
        sys.exit(-1)
   
    # Converts the hex representation of a string into the actual bytes
    key = sys.argv[1].decode("hex") 

    if (len(key) > 8):
        print "This version of the decoder only works with short keys"
        sys.exit(-1)

    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # Open the file
    # rb means reading in binary mode
    with open(input_file, "rb") as f:
        data = f.read()
    
    # Now we encode the data using the key we've read
    decoded_data = decode(data, key)

    # Open or create the output fule
    # wb means writing binary data
    with open(output_file,"wb") as f:
        f.write(decoded_data)