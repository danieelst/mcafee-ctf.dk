# Playing around with my own encryptions to see if it works.

# Message one:   This message is highly confidential.
# Message two:   The one time pad is perfect.
# Message three: Wow super safe string, unbreakable even!
# Key:           t8r##GCv4rk b%oG8Ysk7L_jkV5K/YsCF2mE?*vS

# It works!

import os

from decode_lib import xor_strings, reveal_vulnerable_data

output_file = 'test_output.txt'

# these were calculated using an online tool, message xor key
c1_hex = '6B01532F371D3C4B22533804097F355B03143050671C4C42450C134705262A03501B5020'
c2_hex = '6541350E0C2D29474B003018230E554245061B405626294C03175020'
c3_hex = '72184F49204D572A2112324E2E4734051F7F6050051A2B4C344F4004411852461333325003055723'

# gave me the string backwards, so we rotate them
c1_asc = bytes.fromhex(c1_hex).decode('utf-8')[::-1]
c2_asc = bytes.fromhex(c2_hex).decode('utf-8')[::-1]
c3_asc = bytes.fromhex(c3_hex).decode('utf-8')[::-1] 

words = ['message', 'unbreakable']

if __name__ == "__main__":
    if os.path.exists(output_file):
        os.remove(output_file)

    for word in words:
        reveal_vulnerable_data(c1_asc, word, c2_asc, output_file)
        reveal_vulnerable_data(c1_asc, word, c3_asc, output_file)
        reveal_vulnerable_data(c2_asc, word, c3_asc, output_file)