hexinput = 0x676f6f64206a6f6221 # "good job!"
xor_hexinput = hexinput^0x666666666666666666
print(hex(xor_hexinput))
