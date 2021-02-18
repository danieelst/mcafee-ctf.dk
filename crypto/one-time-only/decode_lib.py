import io

def read_line_from_file(path, encoding='utf-8'):
    with io.open(path, 'r', encoding=encoding) as f:
        return f.readlines()[0]

def xor_strings(str1, str2, length):
    if length > len(str1) or length > len(str2):
        raise ValueError('Length is too long.')
    s = ""
    for i in range(length):
        s += chr((ord(str1[i]) ^ ord(str2[i])))
    return s

def shift(string, shift_amount):
    return ''.join(chr((ord(char) + shift_amount) % 256) for char in string)

def reveal_vulnerable_data(ci, m, cj, output_file, encoding='utf-8', debug=False, shift_amount=0):
    for i in range(len(ci)):
        if i+len(m) > len(ci):
            break

        c = ci[i:i+len(m)]

        k = xor_strings(c, m, len(c))
        with io.open(output_file, 'a', encoding=encoding) as f:
            diff = i+len(m) - len(cj)
            text = xor_strings(cj[i:i+len(m)] + chr(0)*diff, k, len(k))
            text = shift(text, shift_amount)
            f.write(m + ': ' + text + '\n')
        if debug:
            print(ci)
            print(' '*i + m)
            print(' '*i + c)
            print(' '*i + k)
            print(cj)
            print(' '*i + cj[i:i+len(m)])
            print('{}, {}, {}: {}'.format(m, cj[i:i+len(m)], k, xor_strings(cj[i:i+len(m)] + chr(0)*diff, k, len(k))))