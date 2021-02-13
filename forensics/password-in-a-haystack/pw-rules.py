#Passwords cannot contain 3 consecutive characters of your username nor its reverse. This is case insensitive.
def consecutive_rule(password, username):
    username_rev = username [::-1]

    for x in range (len(username)):
        substr = username[x:x+3]
        if(len(substr) == 3):
            if(substr.casefold() in password):
                return False

    for x in range (len(username_rev)):
        substr = username_rev[x:x+3]
        if(len(substr) == 3):
            if(substr.casefold() in password):
                return False
    return True

#Each password must contain at least 3 unique digits
def unique_digits(password):
    unique = set()

    # go through all characters in string
    for c in password:
        if(c.isdigit()):
            if c not in unique:
                unique.add(c)
		
    if(len(unique) >= 3):
        return True
    return False

#All passwords must be 6-12 printable characters in length
def enforce_len(password):
    pw_len = len(password)
    min_len = 6
    max_len = 12
    
    if(pw_len >= min_len and pw_len <= max_len):
        return True
    return False

with open('output.txt') as fp:
    while True:
        line = fp.readline()
        line = line.strip()
        res = enforce_len(line)
        res2 = unique_digits(line)
        res3 = consecutive_rule(line, "steve557")
        if(res and res2 and res3):
            print("I AM THE KEY:", line)
        if not line:
            break
