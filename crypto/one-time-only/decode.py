# Assume that the encryption is a OTP.
# Try and identify parts of the key.

import io
import os

from decode_lib import read_line_from_file, xor_strings, reveal_vulnerable_data

# Data
folder = './encrypted_files/'
filenames = ['encryption1.txt', 'encryption2.txt', 'encryption3.txt']

encoding = 'utf-8'

output_file = 'output.txt'

words = ['Nebakanezzer', 'AcidicZero']

shift_val = 0

if __name__ == "__main__":
    if os.path.exists(output_file):
        os.remove(output_file)

    # Read in all ciphertexts from the provided files.
    c1 = read_line_from_file(folder + filenames[0])
    c2 = read_line_from_file(folder + filenames[1])
    c3 = read_line_from_file(folder + filenames[2])

    # Attempt to decrypt vulnerable data.
    for word in words:
        reveal_vulnerable_data(c1, word, c2, output_file, shift_amount=shift_val)
        reveal_vulnerable_data(c1, word, c3, output_file, shift_amount=shift_val)
        reveal_vulnerable_data(c2, word, c3, output_file, shift_amount=shift_val)
    
    # Reverse
    c1 = c1[::-1]
    c2 = c2[::-1]
    c3 = c3[::-1]

    # Attempt to decrypt vulnerable data.
    for word in words:
        reveal_vulnerable_data(c1, word, c2, output_file, shift_amount=shift_val)
        reveal_vulnerable_data(c1, word, c3, output_file, shift_amount=shift_val)
        reveal_vulnerable_data(c2, word, c3, output_file, shift_amount=shift_val)