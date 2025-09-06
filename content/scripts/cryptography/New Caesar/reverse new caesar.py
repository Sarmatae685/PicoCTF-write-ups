import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

ENCRYPTED_FLAG = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

def unshift(c, k):
    char_index = ord(c) - LOWERCASE_OFFSET # e.g for ord(b) - offset/ord(a) = 98 - 97 = 1
    key_index = ord(k) - LOWERCASE_OFFSET  # in this way we return the index of the character in the alphabet ALPHABET
    return ALPHABET[(char_index - key_index) % len(ALPHABET)] # in the original cipher was ALPHABET[(t1 + t2) % len(ALPHABET)] that is, we added


def b16_decode(encoded_string):
    decoded_chars = []

    for i in range(0, len(encoded_string), 2): # iterate by 2
        char1 = encoded_string[i]
        char2 = encoded_string[i+1] #but for 1 iteration we will extract 2 characters, the i-th and the next one after it

        val1 = ALPHABET.index(char1)
        val2 = ALPHABET.index(char2)

        binary1 = "{0:04b}".format(val1)
        binary2 = "{0:04b}".format(val2)

        eight_bit_binary = binary1 + binary2

        dec_value_in_ascii = int(eight_bit_binary, 2)

        decoded_char = chr(dec_value_in_ascii)

        decoded_chars.append(decoded_char)

    return "".join(decoded_chars)

print(f"Trying to decrypt for all {len(ALPHABET)} possible keys from ALPHABET: {ALPHABET}\n")

for key_char in ALPHABET: # we will search which of the 16 characters of ALPHABET will be VALID key, so this will be an outer loop
    potential_b16_encoded = "" # first unshift to get the b16_encoded string, and then b16_decode it
    for char in ENCRYPTED_FLAG:
        potential_b16_encoded += unshift(char, key_char)

    # for this key (we got string in base16) apply b16_decode
    potential_flag = b16_decode(potential_b16_encoded)

    if potential_flag != None:
        print(f"Key: {key_char} -> Flag: {potential_flag}")
