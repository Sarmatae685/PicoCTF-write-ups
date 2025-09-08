dec = [432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63]

def mod_inverse(decimal, module):
    #calculate the usual modulus.
    basic_mod = decimal % module
    return pow(basic_mod, -1, 41)

decoded_string = ""
for d in dec:
    d_mod_inverse = mod_inverse(d, 41)
    if d_mod_inverse in range(1, 27):
        decoded_string += chr(d_mod_inverse + ord('A') - 1) #A = 65, so we add 64 to the value 1
    elif d_mod_inverse in range(27, 37):
        decoded_string += str(d_mod_inverse - 27)
    else:
        decoded_string += "_"

print(f"picoCTF{{{decoded_string}}}")
