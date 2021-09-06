alphabet="abcdefghijklmnopqrstuvwxyz"
testStr = "Jenny Baby I love you!"
def is_alpha_char(c):
    return (c.lower() in alphabet)

def char_to_num(c):
    return alphabet.index(c.lower())

def num_to_char(x):
    return alphabet[x%26]

def CaesarEncrypt(k, plaintext):
    ciphertext=""
    for j in range(len(plaintext)):
        p=plaintext[j]
        if is_alpha_char(p):
            x= (k + char_to_num(p)) %26
            c=num_to_char(x)
        else:
            c = p
        ciphertext += c
    return ciphertext
        
def CaesarDecrypt(k, ciphertext):
    plaintext=""
    for j in range(len(ciphertext)):
        c=ciphertext[j]
        if is_alpha_char(c):
            x= (char_to_num(c) -k) %26
            p=num_to_char(x)
        else:
            p=c
        plaintext+=p
    return plaintext

# is_alpha_char(alphabet) # return ture
# char_to_num(alphabet) # return 0 
# num_to_char(2) # if x == 0 return 'a' ; x == 1 return 'b' etc.

CaesarEncrypt(13, testStr) #return 'jrypbzr gb zl frphevgl pbhefr!'

cipherStr = "wraal onol v ybir lbh!"
CaesarDecrypt(13, cipherStr)
